<template Lang="html">
	<div class="container">
		<div class="row">
			<div class="col text-left">
				<h2>Listado de libros</h2>
				<div class="col-md-12">
					<b-table striped hover :items="books" :fields="fields">
						<template slot="action" slot-scope="row">
							<b-button size="sm" variant="primary">	Editar
							</b-button>
						</template>
					</b-table>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	data() {
		return {
			fields: [
				{ key: 'id', label: 'Id' },
				{ key: 'title', label: 'Titulo' },
				{ key: 'summary', label: 'Descriccion' },
				{ key: 'isbn', label: 'ISBN' },
				{ key: 'author', label: 'Autor' },
				{ key: 'action', label: 'Accion' }
			],
			books: []
		}
	},
	methods: {
		getBooks() {
			const path = 'http://3.15.13.45:8000/api/v1.0/books/'
			axios.get(path).then((response) => {
				this.books = response.data
			})
			.catch((error) => {
				console.log(error)
			})
		}
	},

	created(){
		this.getBooks()
	}
	
}
</script>

<style lang="css" scoped>
</style>