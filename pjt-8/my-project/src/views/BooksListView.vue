<template>
  <div class="container">
    <h1>도서 목록</h1>

    <!-- 검색창 -->
    <div class="search-box">
      <input
        type="text"
        v-model="searchKeyword"
        placeholder="도서 제목 또는 저자 검색"
        class="search-input"
      />
    </div>

    <!-- 카테고리 필터 -->
    <div class="category-filter">
      <button
        v-for="cat in categories"
        :key="cat.pk"
        @click="selectedCategory = cat.pk"
        :class="{ active: selectedCategory === cat.pk }"
        class="category-button"
      >
        {{ cat.fields.name }}
      </button>
    </div>

    <!-- 도서 목록 -->
    <div class="books-list">
      <div
        v-for="book in filteredBooks"
        :key="book.pk"
        @click="goToBookDetail(book.pk)"
        class="book-card"
      >
        <h3 class="book-title">{{ book.fields.title }}</h3>
        <p class="book-author">저자: {{ book.fields.author }}</p>
        <p class="book-category">카테고리: {{ getCategoryName(book.fields.category) }}</p>
      </div>

      <p v-if="filteredBooks.length === 0" class="no-result">
        검색 결과가 없습니다.
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import booksData from '@/assets/books.json'
import categoriesData from '@/assets/categories.json'

const router = useRouter()

const books = ref([])
const categories = ref([])
const selectedCategory = ref(0)
const searchKeyword = ref('')

onMounted(() => {
  books.value = booksData
  categories.value = categoriesData
})

const filteredBooks = computed(() => {
  return books.value.filter(book => {
    const matchesCategory = selectedCategory.value === 0 || book.fields.category === selectedCategory.value
    const keyword = searchKeyword.value.trim().toLowerCase()
    const matchesKeyword =
      book.fields.title.toLowerCase().includes(keyword) ||
      book.fields.author.toLowerCase().includes(keyword)
    return matchesCategory && matchesKeyword
  })
})

const getCategoryName = (id) => {
  const cat = categories.value.find(c => c.pk === id)
  return cat ? cat.fields.name : '기타'
}

const goToBookDetail = (bookId) => {
  router.push(`/books/${bookId}`)
}
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 20px auto;
  padding: 0 15px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}

.search-box {
  margin-bottom: 20px;
}

.search-input {
  width: 100%;
  padding: 10px 15px;
  font-size: 1rem;
  border: 1.5px solid #ddd;
  border-radius: 6px;
  transition: border-color 0.3s ease;
}

.search-input:focus {
  outline: none;
  border-color: #4a90e2;
  box-shadow: 0 0 5px rgba(74, 144, 226, 0.5);
}

.category-filter {
  display: flex;
  gap: 10px;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 25px;
}

.category-button {
  background-color: #f0f0f0;
  border: none;
  padding: 8px 15px;
  border-radius: 20px;
  font-size: 0.9rem;
  cursor: pointer;
  color: #555;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.category-button:hover {
  background-color: #cce4f7;
  color: #2a69ac;
}

.category-button.active {
  background-color: #4a90e2;
  color: white;
  font-weight: 600;
  box-shadow: 0 2px 6px rgba(74, 144, 226, 0.6);
}

.books-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.book-card {
  padding: 15px 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.2s ease, box-shadow 0.2s ease;
}

.book-card:hover {
  background-color: #f9faff;
  box-shadow: 0 4px 12px rgba(74, 144, 226, 0.15);
}

.book-title {
  margin: 0 0 5px 0;
  font-size: 1.2rem;
  color: #1a1a1a;
}

.book-author,
.book-category {
  margin: 2px 0;
  color: #666;
  font-size: 0.9rem;
}

.no-result {
  text-align: center;
  color: #999;
  font-style: italic;
  margin-top: 30px;
}
</style>