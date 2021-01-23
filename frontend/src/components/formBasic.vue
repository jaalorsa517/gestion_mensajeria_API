<template lang="pug">
	form#form-basic(@submit.prevent="onSubmit")
		.info(v-show="errors.length")
			ul(v-for="error in errors")
				li {{error}}
		h2 {{title}}
		input.username(autocomplete="username" name="username" v-model="username" placeholder="Nombre de usuario")
		input.password(type="password" name="username" v-model="password" placeholder="Contraseña")
		input.submit(type="submit" value="Confirmar")
		slot
</template>

<script>
import { post, get } from "@scripts/consumer_api.js";

export default {
  name: "FormBasic",
  props: {
    title: {
      type: String,
      required: true,
    },
  },
  data: function() {
    return {
      username: "",
      password: "",
      response: null,
      errors: [],
    };
  },
  methods: {
    onSubmit: function() {
      if (this.validate(this.username) && this.validate(this.password)) {
				this.axios.get('localhost:5000/api/v1/')
				// post("/signin", { username: this.username, password: this.password })
        //   .then((response) => console.log("respuesta es " + response))
        //   .catch((error) => console.log(error.toJSON()));
      } else {
        this.errors.push("Rellene los campos");
        setTimeout(() => {
          this.errors.pop();
        }, 3000);
      }
    },
    validate: (data) => (data ? true : false),
  },
};
</script>

<style lang="stylus">

#form-basic
	column-center()
	size-box(300px,auto)
	min-width 300px
	max-width 300px
	margin auto
	padding 10px
	border-radius 10px
	border-top 10px solid color-1
	shadow-box()

	input
		margin-roof-floor(10px)

	.submit
		font-weight bold
.info
	size-box(100%,auto)
	font-size 1em
	text-align start
	color color-2
	border-radius 15px
	background-color color-1
</style>
