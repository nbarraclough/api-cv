<template>
<div>
  <h1>Welcome Dick Head</h1>
  {{ message }}

  <button @click="doSomethingClever()">Click Me</button>
</div>
</template>
<style>

</style>
<script>
export default {
       data() {
            return {
              message:'This is a test message',
            }
        },
        mounted() {
         console.log('Component');
        },

        methods: {

          doSomethingClever() {
            this.message = 'Updated the message'

          }
        }
    }
</script>