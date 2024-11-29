<template>
    <div>
        <h1>Registro</h1>
        <form @submit.prevent="registerUser">
            <input v-model="email" type="email" placeholder="Email" required />
            <input v-model="fullName" type="text" placeholder="Nombre Completo" required />
            <input v-model="phone" type="text" placeholder="Teléfono" />
            <button type="submit">Registrar</button>
        </form>
        <p v-if="message">{{ message }}</p>
    </div>
</template>

<script>
import axios from '@/api/axios';

export default {
    name: 'RegisterForm',
    data() {
        return {
            email: '',
            fullName: '',
            phone: '',
            message: '',
        };
    },
    methods: {
        async registerUser() {
            try {
                const response = await axios.post('/register/', {
                    email: this.email,
                    full_name: this.fullName,
                    phone: this.phone,
                });
                this.message = response.data.message;
            } catch (error) {
                this.message = error.response.data.message;
            }
        },
    },
};
</script>