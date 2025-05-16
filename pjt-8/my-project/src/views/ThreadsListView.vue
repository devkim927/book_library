<template>
  <div class="threads-container">
    <h1>전체 스레드 목록</h1>

    <!-- 카테고리 필터링 -->
    <div class="category-filter">
      <label for="category">카테고리:</label>
      <select id="category" v-model="selectedCategory">
        <option value="전체">전체</option>
        <option v-for="category in categories" :key="category.id" :value="category.name">
          {{ category.name }}
        </option>
      </select>
    </div>

    <!-- 스레드 목록 -->
    <div class="threads-list">
      <div v-for="thread in filteredThreads" 
      :key="thread.id" class="thread-card" @click="goToDetail(thread.id)">
        <h3>{{ thread.title }}</h3>
        <p>{{ thread.content }}</p>
        <p>{{ thread.date }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import threadsData from '@/assets/books.json';
import categoriesData from '@/assets/categories.json';

const router = useRouter();
const threads = ref([]);
const categories = ref(categoriesData);
const selectedCategory = ref('전체');

onMounted(() => {
  threads.value = threadsData;
});

// 카테고리 필터링
const filteredThreads = computed(() => {
  if (selectedCategory.value === '전체') {
    return threads.value;
  }
  return threads.value.filter(thread => thread.category === selectedCategory.value);
});

// 상세 페이지 이동
const goToDetail = (threadId) => {
  router.push(`/threads/${threadId}`);
};
</script>


<style scoped>
.threads-container {
  padding: 20px;
}

.category-filter {
  margin-bottom: 20px;
}

.threads-list {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
}

.thread-card {
  border: 1px solid #ccc;
  padding: 15px;
  border-radius: 8px;
  cursor: pointer;
}

.thread-card:hover {
  background-color: #f0f0f0;
}
</style>
