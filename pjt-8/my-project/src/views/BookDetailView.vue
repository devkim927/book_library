<template>
<div v-if="book" class="book-detail">
    <h1>{{ book.title }}</h1>
    <p><strong>저자:</strong> {{ book.author }}</p>
    <p><strong>출판사:</strong> {{ book.publisher }}</p>
    <p><strong>출판일:</strong> {{ book.publishedDate }}</p>
    <p><strong>ISBN:</strong> {{ book.isbn }}</p>

    <!-- <h3>주변 도서관 정보</h3>
    <div id="map" class="map-container"></div>

    <ul v-if="libraries.length">
    <li v-for="library in libraries" :key="library.place_id">
        {{ library.name }} - {{ library.vicinity }}
    </li>
    </ul> -->
</div>
<div v-else>
    <p>도서 정보를 불러오는 중...</p>
</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import booksData from '@/assets/books.json';
import { Loader } from '@googlemaps/js-api-loader';

const route = useRoute();
const book = ref(null);
const userLocation = ref(null);
const map = ref(null);
const libraries = ref([]);

onMounted(() => {
  const bookId = route.params.bookId;
  book.value = booksData.find(b => b.id === bookId);
})
//   // 사용자 위치 가져오기
//   if (navigator.geolocation) {
//     navigator.geolocation.getCurrentPosition((position) => {
//       userLocation.value = {
//         lat: position.coords.latitude,
//         lng: position.coords.longitude,
//       };
//       initializeMap();
//     });
//   }
// });

// // Google Maps 초기화
// const initializeMap = async () => {
//   const loader = new Loader({
//     apiKey: import.meta.env.VITE_GOOGLE_MAPS_API_KEY,
//     version: 'weekly',
//   });

//   await loader.load();

//   const google = window.google;
//   map.value = new google.maps.Map(document.getElementById('map'), {
//     center: userLocation.value,
//     zoom: 15,
//   });

//   searchLibraries();
// };

// // 주변 도서관 검색
// const searchLibraries = () => {
//   const service = new window.google.maps.places.PlacesService(map.value);
//   const request = {
//     location: userLocation.value,
//     radius: 5000,
//     type: 'library',
//   };

//   service.nearbySearch(request, (results, status) => {
//     if (status === window.google.maps.places.PlacesServiceStatus.OK) {
//       libraries.value = results;
//     }
//   });
// };
</script>


<style scoped>
.map-container {
  width: 100%;
  height: 400px;
  margin-top: 20px;
  border-radius: 10px;
}
</style>
