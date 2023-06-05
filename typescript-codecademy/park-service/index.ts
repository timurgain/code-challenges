import {
  RaccoonMeadowsVolunteers,
  RaccoonMeadowsActivity,
  raccoonMeadowsVolunteers,
} from "./raccoon-meadows-log";

import {
  WolfPointVolunteers,
  WolfPointActivity,
  wolfPointVolunteers,
} from "./wolf-point-log";

type CombinedActivity = RaccoonMeadowsActivity | WolfPointActivity;

type Volunteers = {
  id: number;
  name: string;
  activities: CombinedActivity[];
};

type resultVolunteersData = {
  id: number;
  name: string;
  hours: number;
};

function combineVolunteers(
  volunteers: (RaccoonMeadowsVolunteers | WolfPointVolunteers)[]
) {
  return volunteers.map((volonteer) => {
    let id = volonteer.id;
    if (typeof id === "string") {
      id = parseInt(id, 10);
    }
    return { id: id, name: volonteer.name, activities: volonteer.activities };
  });
}

function calculateHours(volunteers: Volunteers[]) {
  return volunteers.map((volunteer) => {
    let hours = 0;

    volunteer.activities.forEach((activity) => {
      function isVerified(verified: boolean | string) {
        if (typeof verified === "boolean") {
          return verified;
        }
        if (typeof verified === "string") {
          return verified === "Yes" ? true : false;
        }
      }
      function getHours(activity: CombinedActivity) {
        if ("time" in activity) {
          return activity.time;
        }
        if ("hours" in activity) {
          return activity.hours;
        }
      }

      if (isVerified(activity.verified)) {
        hours += getHours(activity);
      }
    });

    return {
      id: volunteer.id,
      name: volunteer.name,
      hours: hours,
    };
  });
}

const byHours = (a: resultVolunteersData, b: resultVolunteersData) =>
  a.hours - b.hours;

const combinedVolunteers = combineVolunteers(
  [].concat(wolfPointVolunteers, raccoonMeadowsVolunteers)
);

// main
const result = calculateHours(combinedVolunteers).sort(byHours);
console.log(result);
