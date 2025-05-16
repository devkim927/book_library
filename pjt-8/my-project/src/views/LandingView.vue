<template>
  <div class="landing-container">
    <nav class="navigation">
      <h1>도서 커뮤니티</h1>
      <ul>
        <li v-for="section in sections" 
        :key="section.path" 
        @click="navigateTo(section.path)">
        {{ section.title }}
        </li>
      </ul>
    </nav>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const sections = ref([
  { title: '도서 목록', path: '/books' },
  { title: '스레드 목록', path: '/threads' }
]);

const navigateTo = (path) => {
  router.push(path);
};
</script>

<style scoped>
.landing-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.navigation ul {
  list-style: none;
  padding: 0;
}

.navigation li {
  cursor: pointer;
  padding: 10px;
  font-weight: bold;
}
</style>