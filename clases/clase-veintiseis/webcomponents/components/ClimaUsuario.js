class ClimaUsuario extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });

    this.shadowRoot.innerHTML = `
      <style>
       :host {
  display: block;
  height: 100%;
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

.card {
  position: relative;
  overflow: hidden;
  font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial;
  width: 100%;
  min-height: 260px;
  padding: 28px;
  border-radius: 20px;

  background:
    linear-gradient(145deg, rgba(15, 23, 42, 0.96), rgba(30, 41, 59, 0.92)),
    linear-gradient(135deg, rgba(59, 130, 246, 0.2), rgba(45, 212, 191, 0.15));
  color: white;

  box-shadow:
    0 22px 45px rgba(2, 6, 23, 0.34),
    inset 0 1px 0 rgba(255, 255, 255, 0.05);

  border: 1px solid rgba(148, 163, 184, 0.2);

  text-align: center;
}

.card::after {
  content: "";
  position: absolute;
  left: -48px;
  top: -58px;
  width: 180px;
  height: 180px;
  border-radius: 999px;
  background: rgba(59, 130, 246, 0.2);
  pointer-events: none;
}

.title {
  position: relative;
  font-size: 13px;
  color: #99f6e4;
  font-weight: 800;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  margin-bottom: 12px;
}

.temp {
  position: relative;
  font-size: 78px;
  line-height: 1;
  font-weight: 900;
  margin: 18px 0 16px;
  color: #f8fafc;
  text-shadow: 0 0 24px rgba(59, 130, 246, 0.35);
}

.desc {
  position: relative;
  font-size: 16px;
  margin-bottom: 8px;
  color: #e2e8f0;
}

.status {
  position: relative;
  font-size: 12px;
  display: inline-flex;
  padding: 7px 11px;
  border-radius: 999px;
  margin-top: 10px;
  color: #cbd5e1;
  background: rgba(15, 23, 42, 0.42);
  border: 1px solid rgba(148, 163, 184, 0.18);
}
      </style>

      <div class="card">
        <div class="title">Clima actual</div>
        <div class="desc" id="place">Detectando ubicación...</div>
        <div class="temp" id="temp">--°</div>
        <div class="desc" id="weather">--</div>
        <div class="status" id="status">Inicializando...</div>
      </div>
    `;
  }

  connectedCallback() {
    this.place = this.shadowRoot.querySelector("#place");
    this.temp = this.shadowRoot.querySelector("#temp");
    this.weather = this.shadowRoot.querySelector("#weather");
    this.status = this.shadowRoot.querySelector("#status");

    this.getLocation();
  }

  getLocation() {
    if (!navigator.geolocation) {
      this.status.textContent = "Geolocalización no soportada";
      return;
    }

    this.status.textContent = "Obteniendo ubicación...";

    navigator.geolocation.getCurrentPosition(
      (pos) => this.fetchWeather(pos.coords.latitude, pos.coords.longitude),
      (err) => {
        this.status.textContent = "No se pudo obtener ubicación";
      }
    );
  }

  async fetchWeather(lat, lon) {
    try {
      this.status.textContent = "Consultando clima...";

      const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`;

      const res = await fetch(url);
      const data = await res.json();

      const w = data.current_weather;

      this.temp.textContent = `${Math.round(w.temperature)}°C`;
      this.weather.textContent = this.getWeatherLabel(w.weathercode);
      this.place.textContent = `Lat: ${lat.toFixed(2)} / Lon: ${lon.toFixed(2)}`;
      this.status.textContent = "Actualizado";
    } catch (e) {
      this.status.textContent = "Error cargando clima";
    }
  }

  getWeatherLabel(code) {
    const map = {
      0: "Despejado ☀️",
      1: "Mayormente despejado",
      2: "Parcialmente nublado",
      3: "Nublado ☁️",
      45: "Neblina",
      48: "Neblina",
      51: "Llovizna ligera 🌧️",
      61: "Lluvia 🌧️",
      80: "Chubascos",
      95: "Tormenta ⛈️"
    };

    return map[code] || "Condición desconocida";
  }
}

customElements.define("clima-usuario", ClimaUsuario);
