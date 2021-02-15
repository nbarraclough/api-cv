<template>
  <div>
    <h1 class="message">Welcome Dick Head</h1>
    {{ message }} <br>
    {{ message_two }}

    <button @click="doSomethingClever()">Click Me</button>

  </div>
</template>

<script>

export default {
       data() {
            return {
              message:'This is a test message',
              message_two:'This is message two',

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