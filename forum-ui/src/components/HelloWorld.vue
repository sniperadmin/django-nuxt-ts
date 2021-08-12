<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="logoSrc"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          <div>Welcome to the Vuetify 3 Alpha</div>
        </h1>

        <h2 class="mb-4">Departments</h2>

        <v-row class="w-100 border h-50" align="center" justify="center">
          <v-sheet
            v-for="dep in deps || []"
            :key="dep.id"
            :elevation="1"
            class="mx-auto mb-3"
            height="100"
            width="100"
          >
            <v-container style="height: 100%">
              <v-row class="mt-5" align="center" justify="center">
                <h3>
                  {{dep.name}}
                </h3>
              </v-row>
            </v-container>
          </v-sheet>
        </v-row>

        <v-btn color="primary" :loading="loading" @click="addDepartment">
          click to add a department
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import logo from '../assets/logo.svg'
import DepartmentDataService from '../services/dataServices'
import { defineComponent, ref, onMounted } from "vue"
import faker from "faker"
import alerts from "@/mixins/alerts.js"

export default defineComponent({
  name: 'HelloWorld',
  setup() {
    const logoSrc = ref(logo)
    let deps = ref<object[]>([])
    const { alertSuccess, alertFailure } = alerts()
    const loading = ref<boolean>(false)

    const getDepartments = async (): Promise<object[]|void> => {
      loading.value = true
      return await DepartmentDataService
      .getAll().then(async (res: object): Promise<object[]> => {
        console.log("res => ", res);
        deps.value = res.data;
        loading.value = false
        return await res.data;
      })
      .catch((e: object) => {
        loading.value = false
        alertFailure()
      })
    }

    const addDepartment = async () => {
      const newCompanyName = faker.company.companyName()
      loading.value = true
      return await DepartmentDataService
      .create({ name: newCompanyName })
      .then(() => {
        loading.value = false
        alertSuccess()
        getDepartments()
      })
      .catch(() => {
          loading.value = false
          alertFailure()
        })
    }

    onMounted(getDepartments)

    return {
      logoSrc,
      deps,
      addDepartment,
      loading
    }
  }
})
</script>
