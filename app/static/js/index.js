$(document).ready(function() {
    // create datatable of all users from the api endpoint
    const apiEndpoint =  `http://${window.location.host}/api/users`;
    const usersDataTable = $('#users-example').DataTable({
        ajax: {
            url: apiEndpoint,
            dataSrc: '',
        },
        columns: [
            {data: "id"},
            {data: "last_login"},
            {data: "is_superuser"},
            {data: "username"},
            {data: "first_name"},
            {data: "last_name"},
            {data: "email"},
            {data: "is_staff"},
            {data: "is_active"},
            {data: "date_joined"},
            {data: "groups"},
            {data: "user_permissions"},
        ]
    });

    // connect to web socket which messages every time change made to User table
    const wsEndpoint = `ws://${window.location.host}/ws/app/users`;
    const usersSocket = new WebSocket(wsEndpoint);

    // refresh ajax source from API every time message is received
    usersSocket.onmessage = function(event) {
        console.log('reloading table...')
        usersDataTable.ajax.reload();
        console.log('success!')
    }
});