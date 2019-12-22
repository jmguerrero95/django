<template Lang="html">
	<div class="container">
		<div class="row">
			<div class="col text-left">
				<h2>Editar Libro</h2>
			</div>
		</div>
	<div class="row">
		<div class="col">
			<div class="card">
				<div class="card-body">
					<form @submit="onSubmit">
						<div class="form-group row">
							<label for="title" class="col-sm-2 col-form-label">Titulo</label>
							<div class="col-sm-6">
								<input type="text" placeholder="Titulo" name="title" class="form-control" v-model.trim="form.title">
							</div>
						</div>
						<div class="form-group row">
							<label for="summary" class="col-sm-2 col-form-label">Descripción</label>
							<div class="col-sm-6">
								<textarea name="summary" class="form-control" placeholder="Descripción" rows="3" v-model.trim="form.summary"></textarea>
							</div>
						</div>
						<div class="form-group row">
							<label for="isbn" class="col-sm-2 col-form-label">ISBN</label>
							<div class="col-sm-6">
								<input type="text" placeholder="ISBN" name="isbn" class="form-control" v-model.trim="form.isbn">
							</div>
						</div>
						<div class="rows">
							<div class="col text-left">
								<b-button type="submit" variant="primary">Editar</b-button>
								<b-button type="submit">Cancelar</b-button>	
							</div>
						</div>
						
					</form>
				</div>
				
			</div>
			
		</div>
	</div>
	</div>
</template>

<script>
	import axios from 'axios'
	import swal from 'sweetalert'
	export default{
		data() {
			return {
				bookId: this.$route.params.bookId,
				form: {
					title: '',
					summary: '',
					isbn: '',
					genre: [2]
				}
			}
		},
		methods: {
			onSubmit(evt){
				evt.preventDefault()

				const path =  `http://localhost:8000/api/v1.0/books/${this.bookId}/`
				console.log(path)
				axios.put(path, this.form).then((response) => {
					this.form.title = response.data.title
					this.form.summary = response.data.summary
					this.form.isbn = response.data.isbn
					this.form.genre = response.data.genre

					swal("actualizado correctamente!", "", "success")
				})
				.catch((error) => {
					console.log(error)
				})	
			},

			getBook (){
				const path =  `http://localhost:8000/api/v1.0/books/${this.bookId}/`
				console.log("prueba")
				axios.get(path).then((response) => {
					this.form.title = response.data.title
					this.form.summary = response.data.summary
					this.form.isbn = response.data.isbn
				})
				.catch((error) => {
					console.log(error)
				})	
			}
		},
		created(){
			this.getBook()
		}
	}
</script>

<style lang="css" scoped>
</style>