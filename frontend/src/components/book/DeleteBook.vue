<template Lang="html">
	<div class="container">	
		<div class="row">	
			<div class="col">
				<h3>¿Estas seguro que deseas eliminarlo?</h3>
				<p>Titulo : {{this.element.title}}</p>
				<p>Descripción : {{this.element.summary}}</p>	
			</div>

		</div>
		<div class="row">
			<div class="col">
				<b-button v-on:click="deleteBook" variant="danger">Eliminar</b-button>
			</div>
		</div>
	</div>
</template>

<script type="text/javascript">
	import axios from 'axios';
	import swal from 'sweetalert'
	export default {
		data () {
			return{
				bookId: this.$route.params.bookId,
				element: {
					title: '',
					summary: ''
				}
			}
		},
	methods: {
		getBook (){
				const path =  `http://localhost:8000/api/v1.0/books/${this.bookId}/`
				console.log("prueba")
				axios.get(path).then((response) => {
					this.element.title = response.data.title
					this.element.summary = response.data.summary
				})
				.catch((error) => {
					console.log(error)
				})	
			},
			deleteBook () {
				const path =  `http://localhost:8000/api/v1.0/books/${this.bookId}/`
				axios.delete(path).then((response) => {
					location.href = '/books'
				})
				.cath((error) => {
					swal("No es posible eliminar el libro", "", "error")
				})
				}
	},
	created() {
		this.getBook()
	}
}
</script>

<style lang=css scoped>
</style>