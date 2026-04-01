import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
from geopy.distance import geodesic
from datetime import datetime
import json
import os

# Konfigurasi halaman
st.set_page_config(
    page_title="Peta Masjid STT NF",
    layout="wide"
)

# Judul aplikasi
st.title("Peta Masjid Sekitar STT Terpadu Nurul Fikri")
st.markdown("---")

# Koordinat STT Nurul Fikri (diperbarui sesuai data asli)
STT_NF_KAMPUS_A = (-6.3627193, 106.8443742)
STT_NF_KAMPUS_B = (-6.3528215, 106.8326181)

# Nama file untuk menyimpan data
DATA_FILE = "data_masjid.json"

# Fungsi untuk memuat data dari file JSON
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data
        except:
            # Jika file corrupt, kembalikan data kosong
            return []
    else:
        # Jika file tidak ada, buat file kosong
        save_data([])
        return []

# Fungsi untuk menyimpan data ke file JSON
def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Inisialisasi session state dengan data dari file
if 'masjids' not in st.session_state:
    st.session_state.masjids = load_data()

if 'user_location' not in st.session_state:
    st.session_state.user_location = None

if 'nearest_masjids' not in st.session_state:
    st.session_state.nearest_masjids = []

# Fungsi untuk menghitung jarak
def calculate_distance(lat1, lon1, lat2, lon2):
    return geodesic((lat1, lon1), (lat2, lon2)).kilometers

# Fungsi untuk mendapatkan masjid terdekat
def find_nearest_masjids(user_lat, user_lon, masjids, limit=10):
    masjids_with_distance = []
    
    for masjid in masjids:
        distance = calculate_distance(
            user_lat, user_lon,
            masjid['latitude'], masjid['longitude']
        )
        masjids_with_distance.append({
            **masjid,
            'distance': round(distance, 3)
        })
    
    masjids_with_distance.sort(key=lambda x: x['distance'])
    return masjids_with_distance[:limit]

# Fungsi untuk membuat peta
def create_map(masjids, user_location=None, center_lat=-6.35777, center_lon=106.8385, zoom_start=14):
    m = folium.Map(location=[center_lat, center_lon], zoom_start=zoom_start, tiles='OpenStreetMap')
    
    # Tambahkan marker untuk Kampus A (hijau)
    folium.Marker(
        location=[STT_NF_KAMPUS_A[0], STT_NF_KAMPUS_A[1]],
        popup='<strong>Kampus A - STT Terpadu Nurul Fikri</strong><br>JRPV+QH5, Jl. Setu Indah No.116, Tugu, Cimanggis, Depok',
        tooltip='Kampus A STT NF',
        icon=folium.Icon(color='green', icon='university', prefix='fa')
    ).add_to(m)
    
    # Tambahkan marker untuk Kampus B (hijau tua)
    folium.Marker(
        location=[STT_NF_KAMPUS_B[0], STT_NF_KAMPUS_B[1]],
        popup='<strong>Kampus B - STT Terpadu Nurul Fikri</strong><br>Jl. Lenteng Agung Raya No.20, Jagakarsa, Jakarta Selatan',
        tooltip='Kampus B STT NF',
        icon=folium.Icon(color='darkgreen', icon='university', prefix='fa')
    ).add_to(m)
    
    # Tambahkan marker untuk setiap masjid (biru)
    for masjid in masjids:
        popup_content = f"""
        <div style="font-family: Arial; width: 280px;">
            <h4 style="color: #2E86C1; margin-bottom: 5px;">{masjid['nama']}</h4>
            <p style="margin: 2px 0;"><strong>Alamat:</strong> {masjid['alamat']}</p>
            <p style="margin: 2px 0;"><strong>Koordinat:</strong> {masjid['latitude']:.7f}, {masjid['longitude']:.7f}</p>
            <p style="margin: 2px 0;"><strong>Info:</strong> {masjid['info']}</p>
            {'<p style="margin: 2px 0; color: #E74C3C;"><strong>Jarak dari Anda:</strong> ' + str(masjid.get('distance', 'N/A')) + ' km</p>' if 'distance' in masjid else ''}
        </div>
        """
        
        folium.Marker(
            location=[masjid['latitude'], masjid['longitude']],
            popup=folium.Popup(popup_content, max_width=300),
            tooltip=masjid['nama'],
            icon=folium.Icon(color='blue', icon='star', prefix='fa')
        ).add_to(m)
    
    # Tambahkan marker untuk lokasi pengguna jika tersedia (merah)
    if user_location:
        folium.Marker(
            location=[user_location['latitude'], user_location['longitude']],
            popup='Lokasi Anda',
            tooltip='Lokasi Anda',
            icon=folium.Icon(color='red', icon='user', prefix='fa')
        ).add_to(m)
    
    return m

# Fungsi untuk menambah masjid baru
def add_new_masjid(nama, alamat, latitude, longitude, info_tambahan):
    # Cari ID terbesar yang ada
    max_id = max([m['id'] for m in st.session_state.masjids]) if st.session_state.masjids else 0
    
    new_masjid = {
        'id': max_id + 1,
        'nama': nama,
        'alamat': alamat,
        'latitude': latitude,
        'longitude': longitude,
        'info': info_tambahan if info_tambahan else "Tidak ada informasi tambahan"
    }
    
    # Tambahkan ke session state
    st.session_state.masjids.append(new_masjid)
    
    # Simpan ke file JSON
    save_data(st.session_state.masjids)
    
    return new_masjid

# Sidebar untuk navigasi
with st.sidebar:
    st.header("Navigasi")
    page = st.radio(
        "Pilih Halaman:",
        ["Beranda", "Peta Masjid", "Cari Masjid Terdekat", "Tambah Data Masjid", "Data Masjid"]
    )
    
    st.markdown("---")
    st.header("Info Kampus")
    st.info("""
    **Kampus A:**
    Jl. Setu Indah No.116
    Tugu, Cimanggis, Depok
    
    **Kampus B:**
    Jl. Lenteng Agung Raya No.20
    Jagakarsa, Jakarta Selatan
    """)
    
    st.markdown("---")
    st.header("Statistik")
    total_masjid = len(st.session_state.masjids)
    st.metric("Total Masjid", total_masjid)
    
    if total_masjid > 0:
        # Hitung jarak rata-rata ke Kampus A
        distances = []
        for masjid in st.session_state.masjids:
            distance = calculate_distance(masjid['latitude'], masjid['longitude'], 
                                         STT_NF_KAMPUS_A[0], STT_NF_KAMPUS_A[1])
            distances.append(distance)
        
        avg_distance = sum(distances) / len(distances)
        st.metric("Rata-rata Jarak ke Kampus A", f"{avg_distance:.2f} km")

# Halaman Beranda
if page == "Beranda":
    st.header("Aplikasi Peta Masjid Sekitar STT Terpadu Nurul Fikri")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Tentang Aplikasi
        
        Aplikasi ini membantu civitas akademika STT Terpadu Nurul Fikri 
        dalam menemukan masjid-masjid di sekitar kampus A (Depok) dan kampus B (Jakarta Selatan).
        
        ### Fitur Utama:
        
        **Peta Lokasi Masjid**
        - Menampilkan peta interaktif dengan lokasi masjid
        - Titik biru: Masjid
        - Titik hijau: Kampus A dan B STT NF
        - Titik merah: Lokasi Anda
        
        **Pencarian Masjid Terdekat**
        - Cari masjid terdekat dari lokasi tertentu
        - Input koordinat manual atau gunakan lokasi kampus
        - Menghitung jarak ke setiap masjid
        
        **Tambah Data Masjid**
        - Form untuk menambahkan data masjid baru
        - Data langsung disimpan ke database
        - Tidak hilang saat refresh halaman
        
        **Data Masjid**
        - Tabel informasi semua masjid
        - Hitung jarak ke kampus
        - Download data dalam format CSV atau JSON
        """)
    
    with col2:
        st.markdown("### Legenda Peta")
        st.markdown("""
        <div style='background-color: blue; color: white; padding: 8px; margin: 5px; border-radius: 5px;'>
        <strong>⭐ Biru:</strong> Masjid
        </div>
        <div style='background-color: green; color: white; padding: 8px; margin: 5px; border-radius: 5px;'>
        <strong>🏛️ Hijau:</strong> Kampus A STT NF
        </div>
        <div style='background-color: darkgreen; color: white; padding: 8px; margin: 5px; border-radius: 5px;'>
        <strong>🏛️ Hijau Tua:</strong> Kampus B STT NF
        </div>
        <div style='background-color: red; color: white; padding: 8px; margin: 5px; border-radius: 5px;'>
        <strong>👤 Merah:</strong> Lokasi Anda
        </div>
        """, unsafe_allow_html=True)
    
    # Tampilkan peta overview
    st.markdown("---")
    st.subheader("Peta Lokasi Kampus dan Masjid")
    
    if len(st.session_state.masjids) > 0:
        overview_map = create_map(st.session_state.masjids)
    else:
        # Jika belum ada masjid, tampilkan peta dengan kampus saja
        overview_map = create_map([], center_lat=-6.35777, center_lon=106.8385, zoom_start=14)
    
    st_folium(overview_map, width=1200, height=500)
    
    if len(st.session_state.masjids) == 0:
        st.info("Belum ada data masjid. Silakan tambahkan data masjid melalui halaman 'Tambah Data Masjid'.")

# Halaman Peta Masjid
elif page == "Peta Masjid":
    st.header("Peta Masjid Sekitar STT NF")
    
    # Kontrol untuk peta
    col1, col2, col3 = st.columns(3)
    
    with col1:
        view_option = st.selectbox(
            "Pusatkan Peta di:",
            ["Tengah Kampus A & B", "Kampus A", "Kampus B", "Lokasi Anda", "Atur Manual"]
        )
    
    if view_option == "Tengah Kampus A & B":
        center_lat = (STT_NF_KAMPUS_A[0] + STT_NF_KAMPUS_B[0]) / 2
        center_lon = (STT_NF_KAMPUS_A[1] + STT_NF_KAMPUS_B[1]) / 2
        zoom_level = st.slider("Zoom Level", min_value=10, max_value=18, value=14)
    
    elif view_option == "Kampus A":
        center_lat, center_lon = STT_NF_KAMPUS_A
        zoom_level = st.slider("Zoom Level", min_value=10, max_value=18, value=15)
    
    elif view_option == "Kampus B":
        center_lat, center_lon = STT_NF_KAMPUS_B
        zoom_level = st.slider("Zoom Level", min_value=10, max_value=18, value=15)
    
    elif view_option == "Lokasi Anda":
        if st.session_state.user_location:
            center_lat = st.session_state.user_location['latitude']
            center_lon = st.session_state.user_location['longitude']
            zoom_level = st.slider("Zoom Level", min_value=10, max_value=18, value=15)
        else:
            center_lat, center_lon = (STT_NF_KAMPUS_A[0] + STT_NF_KAMPUS_B[0]) / 2, (STT_NF_KAMPUS_A[1] + STT_NF_KAMPUS_B[1]) / 2
            zoom_level = st.slider("Zoom Level", min_value=10, max_value=18, value=14)
            st.info("Lokasi Anda belum ditentukan. Peta dipusatkan di tengah kedua kampus.")
    
    else:  # Atur Manual
        with col2:
            center_lat = st.number_input("Latitude Pusat Peta", value=-6.35777, format="%.7f", step=0.0001)
        with col3:
            center_lon = st.number_input("Longitude Pusat Peta", value=106.8385, format="%.7f", step=0.0001)
        zoom_level = st.slider("Zoom Level", min_value=10, max_value=18, value=14)
    
    # Tampilkan peta
    masjid_map = create_map(
        st.session_state.masjids, 
        st.session_state.user_location,
        center_lat, 
        center_lon, 
        zoom_level
    )
    
    st_folium(masjid_map, width=1200, height=600)
    
    st.markdown(f"**Total {len(st.session_state.masjids)} masjid ditampilkan**")

# Halaman Cari Masjid Terdekat
elif page == "Cari Masjid Terdekat":
    st.header("Cari Masjid Terdekat")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("Cari masjid terdekat dari lokasi tertentu")
        
        lokasi_options = ["Kampus A STT NF", "Kampus B STT NF", "Lokasi Lain"]
        lokasi_pilihan = st.radio("Pilih Lokasi Pencarian:", lokasi_options)
        
        if lokasi_pilihan == "Kampus A STT NF":
            user_lat, user_lon = STT_NF_KAMPUS_A
            lokasi_nama = "Kampus A STT NF"
            
        elif lokasi_pilihan == "Kampus B STT NF":
            user_lat, user_lon = STT_NF_KAMPUS_B
            lokasi_nama = "Kampus B STT NF"
            
        else:  # Lokasi Lain
            col_lat, col_lon = st.columns(2)
            with col_lat:
                user_lat = st.number_input("Latitude", value=-6.35777, format="%.7f", step=0.0001)
            with col_lon:
                user_lon = st.number_input("Longitude", value=106.8385, format="%.7f", step=0.0001)
            
            lokasi_nama = st.text_input("Nama Lokasi", value="Lokasi Saya")
        
        if st.button("Cari Masjid Terdekat", type="primary"):
            st.session_state.user_location = {
                'latitude': user_lat,
                'longitude': user_lon,
                'nama': lokasi_nama
            }
            
            if len(st.session_state.masjids) > 0:
                st.session_state.nearest_masjids = find_nearest_masjids(
                    user_lat, user_lon, st.session_state.masjids
                )
                st.success(f"Menemukan {len(st.session_state.nearest_masjids)} masjid terdekat")
            else:
                st.warning("Belum ada data masjid. Silakan tambahkan data masjid terlebih dahulu.")
    
    with col2:
        if st.session_state.user_location:
            st.markdown("### Lokasi Pencarian")
            st.metric("Nama", st.session_state.user_location['nama'])
            st.metric("Latitude", f"{st.session_state.user_location['latitude']:.7f}")
            st.metric("Longitude", f"{st.session_state.user_location['longitude']:.7f}")
            
            if st.session_state.nearest_masjids:
                nearest = st.session_state.nearest_masjids[0]
                st.metric("Masjid Terdekat", nearest['nama'])
                st.metric("Jarak", f"{nearest['distance']} km")
    
    # Tampilkan hasil jika ada
    if st.session_state.nearest_masjids:
        st.markdown("---")
        
        st.subheader("Daftar Masjid Terdekat")
        
        df_nearest = pd.DataFrame(st.session_state.nearest_masjids)
        df_display = df_nearest[['nama', 'alamat', 'distance']].copy()
        df_display.columns = ['Nama Masjid', 'Alamat', 'Jarak (km)']
        
        st.dataframe(df_display, use_container_width=True)
        
        st.subheader("Peta Masjid Terdekat")
        
        nearest_map = create_map(
            st.session_state.nearest_masjids,
            st.session_state.user_location,
            st.session_state.user_location['latitude'],
            st.session_state.user_location['longitude'],
            15
        )
        
        st_folium(nearest_map, width=1200, height=500)
    
    elif st.session_state.user_location and len(st.session_state.masjids) == 0:
        st.info("Belum ada data masjid. Silakan tambahkan data masjid terlebih dahulu di halaman 'Tambah Data Masjid'.")

# Halaman Tambah Data Masjid
elif page == "Tambah Data Masjid":
    st.header("Tambah Data Masjid Baru")
    
    st.info("Tambahkan data masjid baru di sekitar STT Terpadu Nurul Fikri (Kampus A Depok atau Kampus B Jakarta Selatan)")
    
    with st.form("form_tambah_masjid", clear_on_submit=True):
        st.markdown("### Data Masjid")
        
        col1, col2 = st.columns(2)
        
        with col1:
            nama = st.text_input("Nama Masjid*", placeholder="Contoh: Masjid Al-Muhajirin")
            alamat = st.text_area("Alamat Lengkap*", placeholder="Contoh: Jl. H. Mawi No. 10, Depok")
        
        with col2:
            st.markdown("**Koordinat Masjid**")
            latitude = st.number_input("Latitude*", format="%.7f", value=-6.35777, step=0.00001,
                                     help="Contoh: -6.35777")
            longitude = st.number_input("Longitude*", format="%.7f", value=106.8385, step=0.00001,
                                      help="Contoh: 106.8385")
            
            # Hitung jarak ke Kampus A dan B
            distance_to_a = calculate_distance(latitude, longitude, STT_NF_KAMPUS_A[0], STT_NF_KAMPUS_A[1])
            distance_to_b = calculate_distance(latitude, longitude, STT_NF_KAMPUS_B[0], STT_NF_KAMPUS_B[1])
            
            st.info(f"**Jarak ke Kampus A:** {distance_to_a:.3f} km")
            st.info(f"**Jarak ke Kampus B:** {distance_to_b:.3f} km")
        
        info_tambahan = st.text_input("Informasi Tambahan", 
                                    placeholder="Contoh: Kapasitas 500 jamaah, parkir luas, dekat kampus")
        
        submitted = st.form_submit_button("Simpan Data Masjid", type="primary")
        
        if submitted:
            # Validasi input
            if not nama or not alamat:
                st.error("Nama dan alamat masjid harus diisi")
            elif not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
                st.error("Koordinat tidak valid")
            elif distance_to_a > 10 and distance_to_b > 10:
                st.warning(f"Masjid ini cukup jauh dari kedua kampus (>10 km). Pastikan ini masjid di sekitar STT NF.")
                confirm = st.checkbox("Ya, saya yakin masjid ini berada di sekitar STT NF")
                if not confirm:
                    st.stop()
            else:
                # Tambahkan masjid baru
                new_masjid = add_new_masjid(nama, alamat, latitude, longitude, info_tambahan)
                st.success(f"✅ Data masjid '{nama}' berhasil ditambahkan dan disimpan permanen!")
                
                # Tampilkan peta dengan masjid baru
                st.markdown("---")
                st.subheader("Lokasi Masjid Baru")
                
                new_masjid_map = create_map([new_masjid], center_lat=latitude, center_lon=longitude, zoom_start=16)
                st_folium(new_masjid_map, width=1200, height=400)
                
                # Tampilkan info jarak
                st.markdown(f"**Jarak dari Kampus A:** {distance_to_a:.3f} km")
                st.markdown(f"**Jarak dari Kampus B:** {distance_to_b:.3f} km")
    
    with st.expander("📌 Panduan Mendapatkan Koordinat"):
        st.markdown("""
        ### Cara Mendapatkan Koordinat:
        
        1. **Google Maps:**
           - Buka Google Maps (https://maps.google.com)
           - Cari lokasi masjid
           - Klik kanan pada titik lokasi masjid
           - Pilih "Apa ini?"
           - Koordinat akan muncul (contoh: -6.3627193, 106.8443742)
        
        2. **Koordinat Contoh:**
           - **Kampus A:** -6.3627193, 106.8443742
           - **Kampus B:** -6.3528215, 106.8326181
           - **Sekitar Kampus A:** -6.36 sampai -6.37 (Lat), 106.84 sampai 106.85 (Lon)
           - **Sekitar Kampus B:** -6.35 sampai -6.36 (Lat), 106.83 sampai 106.84 (Lon)
        """)

# Halaman Data Masjid
elif page == "Data Masjid":
    st.header("Data Seluruh Masjid")
    
    if len(st.session_state.masjids) > 0:
        df = pd.DataFrame(st.session_state.masjids)
        
        # Tampilkan semua kolom kecuali id
        display_cols = ['nama', 'alamat', 'latitude', 'longitude', 'info']
        display_df = df[display_cols].copy()
        display_df.columns = ['Nama Masjid', 'Alamat', 'Latitude', 'Longitude', 'Informasi']
        
        # Hitung jarak ke Kampus A dan B
        display_df['Jarak ke Kampus A (km)'] = display_df.apply(
            lambda row: round(calculate_distance(row['Latitude'], row['Longitude'], 
                                               STT_NF_KAMPUS_A[0], STT_NF_KAMPUS_A[1]), 3),
            axis=1
        )
        
        display_df['Jarak ke Kampus B (km)'] = display_df.apply(
            lambda row: round(calculate_distance(row['Latitude'], row['Longitude'], 
                                               STT_NF_KAMPUS_B[0], STT_NF_KAMPUS_B[1]), 3),
            axis=1
        )
        
        # Tentukan masjid terdekat untuk setiap kampus
        display_df['Terdekat Kampus'] = display_df.apply(
            lambda row: 'A' if row['Jarak ke Kampus A (km)'] < row['Jarak ke Kampus B (km)'] else 'B',
            axis=1
        )
        
        # Urutkan berdasarkan jarak ke kampus terdekat
        display_df['Jarak Terdekat'] = display_df.apply(
            lambda row: min(row['Jarak ke Kampus A (km)'], row['Jarak ke Kampus B (km)']),
            axis=1
        )
        
        display_df = display_df.sort_values('Jarak Terdekat')
        
        # Tampilkan dataframe
        st.dataframe(display_df, use_container_width=True, hide_index=True)
        
        # Statistik
        st.markdown("---")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Masjid", len(df))
        with col2:
            avg_distance_a = display_df['Jarak ke Kampus A (km)'].mean()
            st.metric("Rata-rata Jarak ke Kampus A", f"{avg_distance_a:.2f} km")
        with col3:
            avg_distance_b = display_df['Jarak ke Kampus B (km)'].mean()
            st.metric("Rata-rata Jarak ke Kampus B", f"{avg_distance_b:.2f} km")
        with col4:
            dekat_a = len(display_df[display_df['Terdekat Kampus'] == 'A'])
            dekat_b = len(display_df[display_df['Terdekat Kampus'] == 'B'])
            st.metric("Terdekat Kampus A/B", f"{dekat_a}/{dekat_b}")
        
        # Opsi export
        st.markdown("---")
        st.subheader("Ekspor Data")
        
        col_exp1, col_exp2 = st.columns(2)
        
        with col_exp1:
            # Export ke CSV
            csv = display_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"data_masjid_stt_nf_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                type="primary"
            )
        
        with col_exp2:
            # Export ke JSON
            json_data = df.to_json(orient='records', force_ascii=False)
            st.download_button(
                label="Download JSON",
                data=json_data,
                file_name=f"data_masjid_stt_nf_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )
        
        # Tampilkan info file
        st.markdown("---")
        with st.expander("ℹ️ Informasi Penyimpanan Data"):
            st.info(f"Data disimpan di file: **{DATA_FILE}**")
            st.code(f"Jumlah data: {len(st.session_state.masjids)} masjid", language='text')
            
    else:
        st.info("📝 Belum ada data masjid. Silakan tambahkan data masjid pertama melalui halaman 'Tambah Data Masjid'.")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Aplikasi Peta Masjid Sekitar STT Terpadu Nurul Fikri | "
    "Data disimpan permanen di file JSON"
    "</div>",
    unsafe_allow_html=True
)