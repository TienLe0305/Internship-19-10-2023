<script setup>
// const props = defineProps({
//   msg: String
// })

// const emit = defineEmits(['response'])

// // emit('response', 'hello from child')

// const handleButtonClick = () => {
//   emit('response', 'hello from child')
// }
const rawHtml = 'Hello Pandosima'
</script>

<template>
    <p>Using text interpolation: {{ rawHtml }}</p>
    <p>Using v-html directive: <span v-html="rawHtml" style="color: red"></span></p>
</template>
