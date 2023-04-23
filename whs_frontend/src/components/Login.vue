<template>
    <div>
      <h1>Authentification</h1>
      <form @submit.prevent="onSubmit">
        <div>
          <label for="username">Nom d'utilisateur :</label>
          <input id="username" v-model="username" required>
        </div>
        <div>
          <label for="password">Mot de passe :</label>
          <input id="password" type="password" v-model="password" required>
        </div>
        <button type="submit">Se connecter</button>
      </form>
    </div>
  </template>
  
  <script>
  import { login } from '@/api';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      async onSubmit() {
        try {
          await login(this.username, this.password);
          // Redirigez vers la page d'accueil de l'utilisateur après une connexion réussie
          this.$router.push('/home');
        } catch (error) {
          // Affichez l'erreur si la connexion échoue
          alert("Erreur d'authentification.");
        }
      },
    },
  };
  </script>
  