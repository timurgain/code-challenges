import studyGroups from "./studyGroups";
import courses from "./courses";

type Course = {
  id: number,
  studyGroupId: number,
  title: string,
  keywords: string[],
  eventType: string,
}

type studyGroup = {
  id: number,
  courseId: number,
  title: string,
  keywords: string[],
  eventType: string,
}

type SearchEventsOptions = {
  query: number | string,
  eventType: 'courses' | 'groups'
};


function searchEvents(options: SearchEventsOptions) {
  let events: (Course | studyGroup)[]
  events = options.eventType === 'courses' ? courses : studyGroups;
  return events.filter((event) => {
    if (typeof options.query === 'number') {
      return options.query === event.id ? true : false
    }
    if (typeof options.query === 'string') {
      return event.keywords.includes(options.query) ? true : false
    }
  })
}

let enrolledEvents: (Course | studyGroup)[] = []

function enroll(events: (Course | studyGroup)[]) {
  events.forEach(event => enrolledEvents.push(event))
}

function drop(events: (Course | studyGroup)[]) {
  events.forEach((event) => {
    const index = enrolledEvents.indexOf(event);
    enrolledEvents.splice(index, 1);
  })
}

function print(events: (Course | studyGroup)[]) {
  const result: string[] = []
  events.forEach(event => result.push(event.title))
  console.log(result.join('\n'))
}


// main

const filteredEvents = searchEvents({
  query: 2,
  eventType: 'courses'
})

enroll(filteredEvents)
print(enrolledEvents)

drop(enrolledEvents)
print(enrolledEvents)
