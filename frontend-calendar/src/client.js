import config from './config';
import jwtDecode from 'jwt-decode';
import * as moment from 'moment';
import axios from 'axios';



class FastAPIClient {
  constructor(overrides) {
    this.config = {
      ...config,
      ...overrides,
    };
    this.authToken = config.authToken;

    this.login = this.login.bind(this);
    this.apiClient = this.getApiClient(this.config);
  }

  /* ----- Authentication & User Operations ----- */

  /* Authenticate the user with the backend services.
   * The same JWT should be valid for both the api and cms */
  login(username, password) {
    delete this.apiClient.defaults.headers['Authorization'];

    // HACK: This is a hack for scenario where there is no login form
    console.log("----------------LOGIN------------")
    const form_data = new FormData();
    const grant_type = 'password';
    const item = { grant_type, username, password };
    for (const key in item) {
      form_data.append(key, item[key]);
    }
    console.log(form_data);

    console.log("---------------- END LOGIN => fetch ------------")
    return this.apiClient
      .post('/token', form_data)
      .then((resp) => {
        localStorage.setItem('token', JSON.stringify(resp.data));
        return this.fetchUser();
      });
  }




  addEvent(calendar_id, newEvent) {
    const title = newEvent.title;
    const description = "desc";
    const property = "property";
    const type = "leasure";
    const start_date = newEvent.start.toISOString();
    const end_date = newEvent.end.toISOString();
    const form_data_bis = {
      title: title,
      description: description,
      start_date: start_date,
      end_date: end_date,
      property: property,
      type: type
    }
    console.log(form_data_bis);
    return this.apiClient.post(`/calendar/${calendar_id}/add_event`, form_data_bis)
      .then((resp) => { return resp.data });

  }




  fetchUser() {

    console.log("----------------FETCH------------")
    return this.apiClient.get('/user/me').then(({ data }) => {

      localStorage.setItem('user', JSON.stringify(data));
      return data;
    });
  }

  async getCalendar() {
    return await this.apiClient.get('/get_calendars').then(({ data }) => {
      return data;
    });
  }






  removeEvent(event_id) {

  }

  async getEventsCalendar(id) {
    return await this.apiClient.get(`/calendar/${id}`).then(({ data }) => {
      return data;
    });
  }

  register(username, password) {
    const registerData = {
      username,
      password
      // is_active: true,
    };

    return this.apiClient.post('/user', registerData).then(
      (resp) => {
        return resp.data;
      });
  }


  // Logging out is just deleting the jwt.
  logout() {
    // Add here any other data that needs to be deleted from local storage
    // on logout
    localStorage.removeItem('token');
    localStorage.removeItem('user');
  }








  /* ----- Client Configuration ----- */

  /* Create Axios client instance pointing at the REST api backend */
  getApiClient(config) {
    const initialConfig = {
      baseURL: `${config.apiBasePath}`
    };

    console.log("-------------In get api fct-----------------------");
    const client = axios.create(initialConfig);

    // client.get("/").then((resp) => console.log(resp.data));

    client.interceptors.request.use(localStorageTokenInterceptor);
    // client.get("").then((resp) => console.log(resp));
    return client;
  }
}


// every request is intercepted and has auth header injected.
function localStorageTokenInterceptor(config) {
  const headers = {};
  const tokenString = localStorage.getItem('token');


  if (tokenString) {
    const token = JSON.parse(tokenString);
    const isAccessTokenValid =
      JSON.stringify(token) !== JSON.stringify({ error: "invalid credentials" });
    if (isAccessTokenValid) {
      const decodedAccessToken = jwtDecode(token.access_token);
      headers['Authorization'] = `Bearer ${token.access_token}`;
    } else {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      alert('Your login session has expired');
    }
  }
  config['headers'] = headers;
  return config;
}

export default FastAPIClient;

