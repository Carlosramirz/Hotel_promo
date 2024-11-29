<template>
    <div>
        <h1>Iniciar Sesión</h1>
        <form @submit.prevent="login">
            <input v-model="email" type="email" placeholder="Correo electrónico" required />
            <input v-model="password" type="password" placeholder="Contraseña" required />
            <button type="submit">Iniciar Sesión</button>
        </form>
        <p v-if="message">{{ message }}</p>
    </div>
</template>

<script>
import axios from "@/api/axios";
import router from "@/router";

export default {
    name: "AdminLogin",
    data() {
        return {
            email: "",
            password: "",
            message: "",
        };
    },
    methods: {
        async login() {
            try {
                const response = await axios.post("/admin-login/", {
                    email: this.email,
                    password: this.password,
                });
                localStorage.setItem("access", response.data.access);
                localStorage.setItem("refresh", response.data.refresh);

                router.push("/admin-panel");
            } catch (error) {
                this.message = error.response?.data?.error || "Error al iniciar sesión.";
            }
        },
    },
};
</script>

<style>
button {
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
