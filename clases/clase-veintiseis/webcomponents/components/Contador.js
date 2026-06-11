class MiContador extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });

    this.valor = 0;

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

.wrapper {
  position: relative;
  overflow: hidden;
  font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 22px;
  padding: 28px;
  border-radius: 20px;
  width: 100%;
  min-height: 260px;

  background:
    linear-gradient(145deg, rgba(15, 23, 42, 0.96), rgba(30, 41, 59, 0.92)),
    linear-gradient(135deg, rgba(45, 212, 191, 0.2), rgba(96, 165, 250, 0.18));
  color: white;

  box-shadow:
    0 22px 45px rgba(2, 6, 23, 0.34),
    inset 0 1px 0 rgba(255, 255, 255, 0.05);

  border: 1px solid rgba(148, 163, 184, 0.2);
}

.wrapper::before {
  content: "Contador";
  color: #99f6e4;
  font-size: 13px;
  font-weight: 800;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.wrapper::after {
  content: "";
  position: absolute;
  right: -44px;
  bottom: -64px;
  width: 180px;
  height: 180px;
  border-radius: 999px;
  background: rgba(20, 184, 166, 0.18);
  pointer-events: none;
}

.valor {
  position: relative;
  font-size: 78px;
  line-height: 1;
  font-weight: 900;
  text-align: center;
  color: #f8fafc;
  letter-spacing: 0;

  text-shadow: 0 0 24px rgba(45, 212, 191, 0.35);
}

.buttons {
  position: relative;
  display: flex;
  gap: 10px;
  justify-content: center;
}

button {
  flex: 1;
  min-height: 46px;
  padding: 10px 12px;
  border-radius: 14px;
  border: 1px solid rgba(255, 255, 255, 0.12);
  cursor: pointer;

  font-weight: 700;
  font-size: 15px;

  transition: all 0.2s ease;
  transform: translateY(0);
}

/* botón + */
#mas {
  background: linear-gradient(135deg, #14b8a6, #0d9488);
  color: white;
}

/* botón - */
#menos {
  background: linear-gradient(135deg, #f97316, #ea580c);
  color: white;
}

/* reset */
#reset {
  background: rgba(148, 163, 184, 0.18);
  color: white;
  backdrop-filter: blur(10px);
}

button:hover {
  transform: translateY(-2px);
  filter: brightness(1.1);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.25);
}

button:active {
  transform: translateY(0px) scale(0.98);
  filter: brightness(0.95);
}
      </style>

      <div class="wrapper">
        <div class="valor" id="display">0</div>

        <div class="buttons">
          <button id="menos">-</button>
          <button id="reset">reset</button>
          <button id="mas">+</button>
        </div>
      </div>
    `;
  }

  connectedCallback() {
    this.display = this.shadowRoot.querySelector("#display");

    this.shadowRoot
      .querySelector("#mas")
      .addEventListener("click", () => this.incrementar());

    this.shadowRoot
      .querySelector("#menos")
      .addEventListener("click", () => this.decrementar());

    this.shadowRoot
      .querySelector("#reset")
      .addEventListener("click", () => this.reset());
  }

  incrementar() {
    this.valor++;
    this.render();
  }

  decrementar() {
    this.valor--;
    this.render();
  }

  reset() {
    this.valor = 0;
    this.render();
  }

  render() {
    this.display.textContent = this.valor;
  }
}

customElements.define("mi-contador", MiContador);
