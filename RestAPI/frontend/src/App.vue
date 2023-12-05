<script setup>
import { reactive, ref, computed, onMounted, watch } from "vue";

let id = 0;
const titleClass = ref("title");
const pElementRef = ref(null)
const count = ref(0);
const text = ref("");
const awesome = ref(true);
const newTodo = ref("");
const hideCompleted = ref(false);
const todos = ref([
  { id: id++, text: "Learn HTML", done: true },
  { id: id++, text: "Learn JavaScript", done: true },
  { id: id++, text: "Learn Vue", done: false },
]);
const todoId = ref(1)
const todoData = ref(null)

async function fetchData() {
  todoData.value = null
  const res = await fetch(
    `https://jsonplaceholder.typicode.com/todos/${todoId.value}`
  )
  todoData.value = await res.json()
}

fetchData()

watch(todoId, fetchData)

onMounted(() => {
  pElementRef.value.textContent = 'mounted!'
})

const filteredTodos = computed(() => {
  return hideCompleted.value ? todos.value.filter((t) => !t.done) : todos.value;
});

const myData = reactive({
  content: "Hello from Vue!",
});

const changeContent = () => {
  myData.content = "Content changed!";
};

function increment() {
  count.value++;
}

// function onInput(e) {
//   text.value = e.target.value;
// }

function toggle() {
  awesome.value = !awesome.value;
}

function addTodo() {
  todos.value.push({ id: id++, text: newTodo.value, done: false });
  newTodo.value = "";
}

function removeTodo(todo) {
  todos.value = todos.value.filter((t) => t !== todo);
}
</script>

<template>
  <div>
    <div class="card">
      <header>
        <h2>Declarative Rendering & Attribute Bindings</h2>
      </header>
      <h1 :class="titleClass">{{ myData.content }}</h1>
      <button @click="changeContent">changeContent</button>
    </div>
    <div class="card">
      <header>
        <h2>Event Listeners</h2>
      </header>
      <button @click="increment">count is: {{ count }}</button>
    </div>
    <div class="card">
      <header>
        <h2>Form Bindings</h2>
      </header>
      <!-- <input :value="text" @input="onInput" placeholder="Type here"> -->
      <input v-model="text" placeholder="Type here" />
      <p>{{ text }}</p>
    </div>
    <div class="card">
      <header>
        <h2>Conditional Rendering</h2>
      </header>
      <button @click="toggle">toggle</button>
      <h3 v-if="awesome">Vue is awesome!</h3>
      <h3 v-else>Oh no 😢</h3>
    </div>
    <div class="card">
      <header>
        <h2>List Rendering</h2>
      </header>
      <form @submit.prevent="addTodo">
        <input v-model="newTodo" />
        <button>Add Todo</button>
      </form>
      <ul>
        <li v-for="todo in filteredTodos" :key="todo.id">
          <input type="checkbox" v-model="todo.done" />
          <span :class="{ done: todo.done }">{{ todo.text }}</span>
          <button @click="removeTodo(todo)">X</button>
        </li>
      </ul>
      <button @click="hideCompleted = !hideCompleted">
        {{ hideCompleted ? "Show all" : "Hide completed" }}
      </button>
    </div>
    <div class="card">
      <header>
        <h2>Lifecycle and Template Refs</h2>
      </header>
      <p ref="pElementRef">Hello Pandosima!</p>
    </div>
    <div class="card">
      <header>
        <h2>Watchers</h2>
      </header>
      <p>Todo id: {{ todoId }}</p>
      <button @click="todoId++" :disabled="!todoData">Fetch next todo</button>
      <p v-if="!todoData">Loading ...</p>
      <pre v-else>{{ todoData }}</pre>
    </div>
  </div>
</template>

<style>
.done {
  text-decoration: line-through;
}

.card {
  border: 1px solid #111010;
  border-radius: 5px;
  padding: 15px;
  margin-bottom: 15px;
}

.card header {
  margin-bottom: 10px;
  color: rgb(0, 162, 255);
}

.title {
  color: red;
  font-size: 24px;
}

button {
  border-radius: 5px;
  margin: 5px;
  padding: 10px;
  cursor: pointer;
}

input {
  padding: 8px;
  margin: 5px;
}

p {
  font-weight: bold;
}
</style>
