import Vue from 'vue';

Vue.component('welcome-component', require('./js/components/WelcomeComponent').default);


import component from './js/components/helloworld.js';
document.body.appendChild(component());




new Vue({
    el: '#app',
});



