<template lang="pug">
	.login-container
		formBasic(title="Ingrese")
			router-link.link(to="/signin") ¿No estás registrado? Regístrese
		
</template>

<script>
import formBasic from '@components/formBasic'

export default {
	name:'LoginView',
	components:{
		formBasic
	}
}
</script>