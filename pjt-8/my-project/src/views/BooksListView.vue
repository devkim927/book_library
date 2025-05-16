<template>
  <div class="books-container">
    <h1>도서 목록</h1>

    <!-- 카테고리 선택 -->
    <div class="category-filter">
      <label for="category">카테고리:</label>
      <select id="category" v-model="selectedCategory">
        <option value="전체">전체</option>
        <option v-for="category in categories" :key="category.id" :value="category.name">
          {{ category.name }}
        </option>
      </select>
    </div>

    <!-- 도서 목록 -->
    <div class="books-list">
      <div v-for="book in filteredBooks" :key="book.id" class="book-card">
        <h3>{{ book.title }}</h3>
        <p>{{ book.author }} | {{ book.publisher }}</p>
        <p>{{ book.publishedDate }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import booksData from '@/assets/books.json';
import categoriesData from '@/assets/categories.json';

const books = ref([]);
const categories = ref(categoriesData);
const selectedCategory = ref('전체');

onMounted(() => {
  books.value = booksData;
});

// 카테고리 필터링
const filteredBooks = computed(() => {
  if (selectedCategory.value === '전체') {
    return books.value;
  }
  return books.value.filter(book => book.category === selectedCategory.value);
});
</script>

<style scoped>
.books-container {
  padding: 20px;
}

.category-filter {
  margin-bottom: 20px;
}

.books-list {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
}

.book-card {
  border: 1px solid #ccc;
  padding: 15px;
  border-radius: 8px;
}
</style>