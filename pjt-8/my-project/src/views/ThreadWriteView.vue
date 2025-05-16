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
import { useRouter, useRoute } from 'vue-router'
import { useThreadStore } from '@/stores/threadStore'
import booksData from '@/assets/books.json'
import categoriesData from '@/assets/categories.json'

const router = useRouter()
const route = useRoute()
const threadStore = useThreadStore()

const title = ref('')
const content = ref('')
const category = ref('')
const book = ref(null)
const categories = ref([])

const bookId = parseInt(route.params.bookId)

onMounted(() => {
  const foundBook = booksData.find(b => b.pk === bookId)
  if (foundBook) {
    book.value = {
      id: foundBook.pk,
      ...foundBook.fields
    }
  }

  categories.value = categoriesData
})

function getCategoryName(id) {
  const category = categories.value.find(c => c.pk === id)
  return category ? category.fields.name : '기타'
}

function submitThread() {
  if (!title.value || !content.value) {
    alert('제목과 내용을 입력해주세요.')
    return
  }

  threadStore.addThread({
    title: title.value,
    content: content.value,
    category: category.value,
    bookId: bookId
  })

  router.push('/threads')
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