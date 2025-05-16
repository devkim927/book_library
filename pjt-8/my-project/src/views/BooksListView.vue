<template>
  <div>
    <h1>도서 목록</h1>

    <!-- 카테고리 필터 -->
    <div>
      <button
        v-for="cat in categories"
        :key="cat.pk"
        @click="selectedCategory = cat.pk"
        :class="{ active: selectedCategory === cat.pk }"
      >
        {{ cat.fields.name }}
      </button>
    </div>

    <!-- 도서 목록 -->
    <div>
      <div
        v-for="book in filteredBooks"
        :key="book.pk"
        @click="goToBookDetail(book.pk)"
        style="cursor: pointer; border: 1px solid #ccc; padding: 10px; margin: 10px 0;"
      >
        <h3>{{ book.fields.title }}</h3>
        <p>저자: {{ book.fields.author }}</p>
        <p>카테고리: {{ getCategoryName(book.fields.category) }}</p>
      </div>
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
const selectedCategory = ref(0) // 기본: '전체' 카테고리

onMounted(() => {
  books.value = booksData
  categories.value = categoriesData
})

const filteredBooks = computed(() => {
  if (selectedCategory.value === 0) {
    return books.value
  }
  return books.value.filter(book => book.fields.category === selectedCategory.value)
})

const getCategoryName = (id) => {
  const cat = categories.value.find(c => c.pk === id)
  return cat ? cat.fields.name : '기타'
}

// 📌 클릭 시 상세 페이지 이동 함수
const goToBookDetail = (bookId) => {
  router.push(`/books/${bookId}`)
}
</script>

<style scoped>
.active {
  font-weight: bold;
  text-decoration: underline;
}
</style>
