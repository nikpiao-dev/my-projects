// Giving Props
// export default function App() {
//     const catalogItems = [
//     {
//       name: "Dan",
//       category: "Developer",
//       website: "dandeveloper.dev"
//     },
//     {
//       name: "Fatima",
//       category: "Doctor",
//       website: "fatimahealth.com"
//     },
//     {
//       name: "Juan",
//       category: "Community Leader",
//       website: "juan.me"
//     }
//   ]
//   return (
//     <div>
//       {catalogItems.map(function (item) {
//         return (
//           <div>
//             <h2>{item.name}</h2>
//             <h3>Specialty: {item.category}</h3>
//             <a href={item.website}>Learn more</a>
//           </div>
//         )
//       })}
//     </div>
//   )
// }


// Notifications

// import Notification from "./Notification.js";

// export default function App() {
//   return (
//     <div>
//   <h1>Notifications</h1>
//   <Notification message="Fatima commented on your post." isRead={true} />
//   <Notification message="Daniel's birthday is today! 🎂" isRead={false} />
//   <Notification message="Rhea just posted on their feed!" isRead={false} />
// </div>

//   );
// }


// Stopwatch

// import React from "react";
// import Stopwatch from "./Stopwatch.js";

// export default function App() {
//   return <Stopwatch />;
// }


// Quiz


import React from "react";
import Quiz from "./Quiz.js"

export default function App() {
  return <Quiz />;
}
