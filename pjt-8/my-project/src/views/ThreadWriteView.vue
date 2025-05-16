<template>
  <div class="thread-write">
    <h1>쓰레드 작성</h1>

    <!-- 도서 정보 카드 -->
    <div v-if="book" class="book-card">
      <h2>{{ book.title }}</h2>
      <p><strong>저자:</strong> {{ book.author }}</p>
      <p><strong>카테고리:</strong> {{ getCategoryName(book.category) }}</p>
    </div>
    <div v-else>
      <p>도서 정보를 불러오는 중입니다...</p>
    </div>

    <!-- 쓰레드 작성 폼 -->
    <form @submit.prevent="submitThread" class="thread-form">
      <label>
        제목:
        <input v-model="title" type="text" required />
      </label>
      <label>
        내용:
        <textarea v-model="content" required rows="6" />
      </label>
      <button type="submit">등록하기</button>
    </form>
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
const title = ref('')
const content = ref('')
const categories = ref([])

onMounted(() => {
  categories.value = categoriesData
  book.value = booksData.find(b => b.id === bookId)
})

const getCategoryName = (id) => {
  const category = categories.value.find(c => c.pk === id)
  return category ? category.fields.name : '기타'
}

const submitThread = () => {
  // 여기서 실제 저장 로직 또는 API 호출 가능
  console.log('쓰레드 등록:', {
    bookId,
    title: title.value,
    content: content.value,
  })

  alert('쓰레드가 등록되었습니다!')
  // 이후 라우터 이동 등 추가 가능
}
</script>

<style scoped>
.thread-write {
  max-width: 600px;
  margin: auto;
  padding: 20px;
}

.book-card {
  background-color: #f8f8f8;
  padding: 16px;
  border-radius: 12px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  margin-bottom: 24px;
}

.thread-form label {
  display: block;
  margin-bottom: 16px;
  font-weight: 600;
}

.thread-form input,
.thread-form textarea {
  width: 100%;
  padding: 8px;
  margin-top: 4px;
  box-sizing: border-box;
}

.thread-form button {
  padding: 10px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
</style>