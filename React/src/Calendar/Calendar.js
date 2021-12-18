import React from 'react'
import FullCalendar from '@fullcalendar/react' // must go before plugins
import dayGridPlugin from '@fullcalendar/daygrid' // a plugin!
 
function Calendar() {
    
    const events = [
        {
            start: '2021-12-01',
            title: 'test event1',
        },
        {
            start: '2022-01-10',
            title: 'test event2',
        }
    ];

    return (
        <>
      <FullCalendar
        plugins={[ dayGridPlugin ]}
        initialView="dayGridMonth"
        weekends={false}
        events={events}
/>
        </>  
    ); 
}

export default Calendar;