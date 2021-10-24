<template>
  <v-row class="fill-height" style="background-color: #E0E0E0; border-radius: 20px;">
    <v-col>
      <v-sheet height="30" style="border-radius: 20px;">
        <v-toolbar
          flat
        >
          <v-btn
            outlined
            class="mr-4"
            color="grey darken-2"
            @click="setToday"
          >
            Today
          </v-btn>
          <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="prev"
          >
            <v-icon small>
              mdi-chevron-left
            </v-icon>
          </v-btn>
          <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="next"
          >
            <v-icon small>
              mdi-chevron-right
            </v-icon>
          </v-btn>
          <v-toolbar-title v-if="$refs.calendar">
            {{ $refs.calendar.title }}
          </v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
      </v-sheet>
      <v-sheet height="600">
        <v-calendar
          ref="calendar"
          v-model="focus"
          color="primary"
          type="category"
          category-show-all
          :categories="categories"
          :events="events"
          :event-color="getEventColor"
          @change="fetchEvents"
        ></v-calendar>
      </v-sheet>
    </v-col>
  </v-row>
</template>


<script>
  export default {
    name: 'Calendar',
    data: () => ({
      focus: '',
      events: [],
      colors: ['var(--main-blue)', 'blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1'],
      names: ['Meeting', 'Holiday', 'PTO', 'Travel', 'Event', 'Birthday', 'Conference', 'Party'],
      categories: [''],
    }),
    mounted () {
      this.$refs.calendar.checkChange()
    },
    methods: {
      getEventColor (event) {
        return event.color
      },
      setToday () {
        this.focus = ''
      },
      prev () {
        this.$refs.calendar.prev()
      },
      next () {
        this.$refs.calendar.next()
      },
      fetchEvents ({ start, end }) {
        const events = []

        const min = new Date(`${start.date}T00:00:00`)
        const max = new Date(`${end.date}T23:59:59`)

        for (let i=3; i<6; i++) {
            const firstTimestamp = new Date(`2021-10-2${i}T09:30:00`)
            console.log(min + max)
            const first = new Date(firstTimestamp - (firstTimestamp % 900000))
            const secondTimestamp = 20 * 900000
            const second = new Date(first.getTime() + secondTimestamp)

            events.push({
            name: 'Terryaki, Baked Beans',
            start: first,
            end: second,
            color: this.colors[0],
            timed: true,
            category: this.categories[this.rnd(0, this.categories.length - 1)],
            description: "hii"
            })
        }

        for (let i=3; i<6; i++) {
            const firstTimestamp = new Date(`2021-10-2${i}T16:30:00`)
            const first = new Date(firstTimestamp - (firstTimestamp % 900000))
            const secondTimestamp = 20 * 900000
            const second = new Date(first.getTime() + secondTimestamp)

            events.push({
            name: 'Tandori Chicken, Fried Rice',
            start: first,
            end: second,
            color: this.colors[0],
            timed: true,
            category: this.categories[this.rnd(0, this.categories.length - 1)],
            description: "hii"
            })
        }
        this.events = events
      },
      rnd (a, b) {
        return Math.floor((b - a + 1) * Math.random()) + a
      },
    },
  }
</script>