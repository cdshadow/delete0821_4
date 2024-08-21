import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit.components.v1 import html

# JavaScript로 사용자의 현재 위치 가져오기
def get_user_location():
    st.markdown(
        """
        <script>
        function getLocation() {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const latitude = position.coords.latitude;
                    const longitude = position.coords.longitude;
                    document.getElementById('lat').value = latitude;
                    document.getElementById('lon').value = longitude;
                    document.getElementById('location-form').submit();
                }
            );
        }
        </script>
        """,
        unsafe_allow_html=True
    )

    html(
        """
        <form id="location-form">
            <input type="hidden" id="lat" name="lat">
            <input type="hidden" id="lon" name="lon">
            <button onclick="getLocation()">현위치(Current Location)</button>
        </form>
        """,
        height=100,
    )

# 위치 좌표 가져오기
lat = st.experimental_get_query_params().get('lat', [None])[0]
lon = st.experimental_get_query_params().get('lon', [None])[0]

# Folium 지도 생성 (입력된 위치 또는 현재 위치를 중심으로 설정)
if lat and lon:
    latitude = float(lat)
    longitude = float(lon)

    map_obj = folium.Map(
        location=[latitude, longitude],  # 현재 위치의 중심 좌표
        zoom_start=15  # 줌 레벨 설정
    )

    # 현위치 마커 추가
    folium.Marker([latitude, longitude], tooltip="Current Location").add_to(map_obj)

    # Streamlit 앱에 지도 표시
    st_folium(map_obj, width=800, height=600)
else:
    st.warning("위치를 찾기 위해 '현위치' 버튼을 눌러주세요.")

# 사용자 위치를 가져오는 버튼 표시
get_user_location()
