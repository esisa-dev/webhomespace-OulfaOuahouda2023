
<template>
    <div>
      <h1>Bienvenue dans votre espace personnel</h1>
      <!-- Ajoutez ici les fonctionnalités supplémentaires (recherche, téléchargement, déconnexion, etc.) -->
      <ul>
        <li v-for="item in directoryContent" :key="item.name">
          {{ item.name }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import { getDirectoryData } from '@/api';
  
  export default {
    data() {
      return {
        directoryContent: [],
      };
    },
    async created() {
      try {
        this.directoryContent = await getDirectoryData();
      } catch (error) {
        // Gérez l'erreur si la récupération du contenu du dossier échoue
        alert("Erreur lors de la récupération du contenu du dossier.");
      }
    },
  };
  </script>
  