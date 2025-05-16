<template>
  <div v-if="book">
    <h1>{{ book.title }}</h1>
    <p><strong>저자:</strong> {{ book.author }}</p>
    <p><strong>출판사:</strong> {{ book.publisher }}</p>
    <p><strong>출판일:</strong> {{ book.pub_date }}</p>
    <p><strong>ISBN:</strong> {{ book.isbn }}</p>
    <p><strong>카테고리:</strong> {{ getCategoryName(book.category) }}</p>
    <p><strong>설명:</strong> {{ book.description }}</p>

  <router-link :to="`/threads/${book.id}/write`">
    <button>이 도서에 대한 쓰레드 작성</button>
  </router-link>
  </div>

  <div v-else>
    <p>도서를 찾을 수 없습니다.</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import booksData from '@/assets/books.json'
import categoriesData from '@/assets/categories.json'

const route = useRoute()
const bookId = parseInt(route.params.bookId)

const book = ref(null)
const categories = ref([])

onMounted(() => {
  const rawBook = booksData.find(b => b.pk === bookId)
  if (rawBook) {
    book.value = {
      id: rawBook.pk,
      title: rawBook.fields.title,
      author: rawBook.fields.author,
      publisher: rawBook.fields.publisher,
      pub_date: rawBook.fields.pub_date,
      isbn: rawBook.fields.isbn,
      category: rawBook.fields.category,
      description: rawBook.fields.description
    }
  }

  categories.value = categoriesData
})

const getCategoryName = (id) => {
  const cat = categories.value.find(c => c.pk === id)
  return cat ? cat.fields.name : '기타'
}
</script>

<style scoped>
button {
  margin-top: 20px;
  padding: 8px 16px;
  font-size: 16px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>