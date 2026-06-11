 class AppHeader extends HTMLElement {
            constructor() {
                super();
                this.attachShadow({ mode: "open" });

                this.shadowRoot.innerHTML = `
      <style>
        :host {
          display: block;
          font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
        }

        *,
        *::before,
        *::after {
          box-sizing: border-box;
        }

        header {
          position: relative;
          overflow: hidden;
          background:
            linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(17, 24, 39, 0.86)),
            linear-gradient(90deg, #14b8a6, #3b82f6);
          color: #ffffff;
          padding: 34px 38px;
          box-shadow: 0 24px 55px rgba(2, 6, 23, 0.35);
          border-radius: 22px;
          margin: 0 0 22px;
          border: 1px solid rgba(148, 163, 184, 0.22);
          min-height: 170px;
          display: flex;
          flex-direction: column;
          justify-content: center;
        }

        header::before {
          content: "";
          position: absolute;
          inset: 14px;
          border-radius: 16px;
          border: 1px solid rgba(255, 255, 255, 0.09);
          pointer-events: none;
        }

        header::after {
          content: "";
          position: absolute;
          right: -42px;
          top: -54px;
          width: 220px;
          height: 220px;
          border-radius: 999px;
          background: rgba(45, 212, 191, 0.18);
          box-shadow: -90px 110px 0 rgba(59, 130, 246, 0.12);
          pointer-events: none;
        }

        h1 {
          position: relative;
          margin: 0;
          max-width: 760px;
          font-size: clamp(2rem, 5vw, 3.8rem);
          line-height: 1;
          font-weight: 850;
          letter-spacing: 0;
        }

        .subtitle {
          position: relative;
          margin-top: 14px;
          max-width: 560px;
          font-size: 1rem;
          color: #cbd5e1;
        }

        .accent {
          color: #67e8f9;
          text-shadow: 0 0 26px rgba(103, 232, 249, 0.35);
        }

        @media (max-width: 640px) {
          header {
            padding: 28px 24px;
            min-height: 150px;
          }
        }
      </style>

      <header>
        <h1>
          Bienvenido a mi sitio de <span class="accent">Web Components</span>
        </h1>
        <div class="subtitle">
          Arquitectura moderna con componentes encapsulados
        </div>
      </header>
    `;
            }
        }

        customElements.define("app-header", AppHeader);
