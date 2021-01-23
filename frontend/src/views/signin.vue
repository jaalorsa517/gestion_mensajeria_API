<template lang="pug">
	.signin-container
		formBasic(title="Regístrese")
			router-link.link(to="/") ¿Ya estás registrado? Ingresa!
</template>

<script>
import formBasic from '@components/formBasic'

export default {
	name:'SigninView',
	components:{
		formBasic
	}
}
</script>