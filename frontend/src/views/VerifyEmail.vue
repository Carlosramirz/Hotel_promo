<template>
    <div>
        <h1>Verificar Email</h1>
        <form @submit.prevent="verifyEmail">
            <input v-model="token" type="text" placeholder="Token" required>
            <input v-model="password" type="password" placeholder="Nueva contraseña" required>
            <button type="submit">Confirmar</button>
        </form>
        <p v-if="message">{{ message }}</p>
    </div>
</template>

<script>
import axios from '@/api/axios';

export default{
    name: 'VerifyEmail',
    data(){
        return{
            token: '',
            password: '',
            message: '',
        };
    },
    methods:{
        async verifyEmail(){
            try{
                const response = await axios.post('/verify-email/', {
                    token: this.token,
                    password: this.password,
                });
                this.message = response.data.message;
            } catch (error){
                this.message = error.response?.data?.error || 'Error al v erificar el correo';
            }
        },
    },
};

</script>