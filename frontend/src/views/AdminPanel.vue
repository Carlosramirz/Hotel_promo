<template>
    <div>
        <h1>Panel de Administración</h1>
        <button @click="generateWinner">Generar Ganador</button>
        <button @click="logout">Cerrar Sesión</button>
        <p v-if="message">{{ message }}</p>
    </div>
</template>

<script>
import axios from "@/api/axios";
import router from "@/router";

export default {
    name: "AdminPanel",
    data() {
        return {
            message: "",
        };
    },
    created() {
        this.checkAuth(); 
    },
    methods: {
        async checkAuth() {
            const token = localStorage.getItem("access");
            if (!token) {
                router.push("/admin-login");
                return;
            }
        },
        async generateWinner() {
            try {
                const token = localStorage.getItem("access");
                const response = await axios.post("/generate-winner/", null, {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                });
                this.message = response.data.message;
            } catch (error) {
                this.message =
                    error.response?.data?.message || "Error al generar el ganador.";
            }
        },
        logout() {
            localStorage.removeItem("access");
            localStorage.removeItem("refresh");
            this.message = "Sesión cerrada.";

            router.push("/admin-login");
        },
    },
};
</script>

<style>
button {
  padding: 10px;
  margin: 5px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
