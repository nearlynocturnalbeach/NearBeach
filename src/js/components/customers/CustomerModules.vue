<template>
	<n-config-provider :theme="getTheme(theme)">
		<div class="card">
			<div class="card-body">
				<!-- The MENU Items -->
				<ul
					class="nav nav-tabs"
					id="misc_module_tabs"
					role="tablist"
				>
					<!-- Associated Projects & Tasks -->
					<li
						class="nav-item"
						role="presentation"
					>
						<button
							class="nav-link active"
							id="associated-objects-tab"
							data-bs-toggle="tab"
							data-bs-target="#associated-objects"
							type="button"
							role="tab"
							aria-controls="home"
							aria-selected="true"
						>
							Associated Objects
						</button>
					</li>
				</ul>
				<hr/>

				<!-- The Modules -->
				<div
					class="tab-content"
					id="misc_module_content"
				>
					<div
						class="tab-pane fade active show"
						id="associated-objects"
						role="tabpanel"
						aria-labelledby="profile-tab"
					>
						<associated-objects
						></associated-objects>
					</div>
				</div>
			</div>
		</div>
	</n-config-provider>
</template>

<script>
import AssociatedObjects from "../modules/sub_modules/AssociatedObjects.vue";
import { mapGetters } from "vuex";

//Mixin
import getThemeMixin from "../../mixins/getThemeMixin";

export default {
	name: "CustomerModule",
	components: {
		AssociatedObjects,
	},
	mixins: [
		getThemeMixin,
	],
	computed: {
		...mapGetters({
			theme: "getTheme",
		}),
	},
};
</script>

<style scoped></style>
