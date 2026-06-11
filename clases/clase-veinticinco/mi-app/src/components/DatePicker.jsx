import { useState, useCallback } from "react";

const MESES = [
  "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre",
];

const DIAS_SEMANA = [
  "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado",
];

function daysInMonth(month, year) {
  return new Date(year, month, 0).getDate();
}

function isLeapYear(year) {
  return year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0);
}

function pad(n) {
  return String(n).padStart(2, "0");
}

function Spinner({ onUp, onDown, children, wide = false }) {
  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 6 }}>
      <button onClick={onUp} style={styles.arrow} aria-label="Subir">▲</button>
      <div style={{ ...styles.segment, minWidth: wide ? 110 : 64 }}>{children}</div>
      <button onClick={onDown} style={styles.arrow} aria-label="Bajar">▼</button>
    </div>
  );
}

export default function DatePicker({ onChange }) {
  const today = new Date();
  const [day, setDay] = useState(today.getDate());
  const [month, setMonth] = useState(today.getMonth() + 1);
  const [year, setYear] = useState(today.getFullYear());
  const [dayInput, setDayInput] = useState(pad(today.getDate()));
  const [yearInput, setYearInput] = useState(String(today.getFullYear()));

  const maxDay = daysInMonth(month, year);

  const clampDay = useCallback(
    (d) => Math.max(1, Math.min(d, daysInMonth(month, year))),
    [month, year]
  );

  const adjustDay = (delta) => {
    const next = ((day - 1 + delta + maxDay) % maxDay) + 1;
    setDay(next);
    setDayInput(pad(next));
    onChange?.({ day: next, month, year });
  };

  const adjustMonth = (delta) => {
    const next = ((month - 1 + delta + 12) % 12) + 1;
    const newMax = daysInMonth(next, year);
    const safeDay = Math.min(day, newMax);
    setMonth(next);
    setDay(safeDay);
    setDayInput(pad(safeDay));
    onChange?.({ day: safeDay, month: next, year });
  };

  const adjustYear = (delta) => {
    const next = Math.max(1, Math.min(year + delta, 9999));
    const newMax = daysInMonth(month, next);
    const safeDay = Math.min(day, newMax);
    setYear(next);
    setYearInput(String(next));
    setDay(safeDay);
    setDayInput(pad(safeDay));
    onChange?.({ day: safeDay, month, year: next });
  };

  const handleDayInput = (e) => {
    setDayInput(e.target.value);
  };

  const handleDayBlur = () => {
    const val = clampDay(parseInt(dayInput, 10) || day);
    setDay(val);
    setDayInput(pad(val));
    onChange?.({ day: val, month, year });
  };

  const handleYearInput = (e) => {
    setYearInput(e.target.value);
  };

  const handleYearBlur = () => {
    const val = Math.max(1, Math.min(parseInt(yearInput, 10) || year, 9999));
    setYear(val);
    setYearInput(String(val));
    onChange?.({ day, month, year: val });
  };

  const setToday = () => {
    const t = new Date();
    setDay(t.getDate());
    setMonth(t.getMonth() + 1);
    setYear(t.getFullYear());
    setDayInput(pad(t.getDate()));
    setYearInput(String(t.getFullYear()));
    onChange?.({ day: t.getDate(), month: t.getMonth() + 1, year: t.getFullYear() });
  };

  const dateObj = new Date(year, month - 1, day);
  const diaSemana = DIAS_SEMANA[dateObj.getDay()];
  const bisiesto = isLeapYear(year);

  return (
    <div style={styles.root}>
      <div style={styles.card}>
        {/* Header */}
        <div style={styles.header}>
          <span style={styles.headerTitle}>Seleccionar fecha</span>
          <button style={styles.todayBtn} onClick={setToday}>Hoy</button>
        </div>

        {/* Spinners */}
        <div style={styles.spinners}>
          {/* Día */}
          <Spinner onUp={() => adjustDay(1)} onDown={() => adjustDay(-1)}>
            <input
              type="text"
              inputMode="numeric"
              maxLength={2}
              value={dayInput}
              onChange={handleDayInput}
              onBlur={handleDayBlur}
              style={styles.input}
              aria-label="Día"
            />
          </Spinner>

          <span style={styles.sep}>/</span>

          {/* Mes */}
          <Spinner onUp={() => adjustMonth(1)} onDown={() => adjustMonth(-1)} wide>
            <div style={{ ...styles.input, cursor: "default", fontSize: 15 }}>
              {MESES[month - 1]}
            </div>
          </Spinner>

          <span style={styles.sep}>/</span>

          {/* Año */}
          <Spinner onUp={() => adjustYear(1)} onDown={() => adjustYear(-1)}>
            <input
              type="text"
              inputMode="numeric"
              maxLength={4}
              value={yearInput}
              onChange={handleYearInput}
              onBlur={handleYearBlur}
              style={{ ...styles.input, fontSize: 16 }}
              aria-label="Año"
            />
          </Spinner>
        </div>

        {/* Labels */}
        <div style={styles.labels}>
          <span style={styles.label}>Día</span>
          <span style={{ ...styles.label, opacity: 0 }}>|</span>
          <span style={{ ...styles.label, minWidth: 110, textAlign: "center" }}>Mes</span>
          <span style={{ ...styles.label, opacity: 0 }}>|</span>
          <span style={styles.label}>Año</span>
        </div>

        {/* Divider */}
        <div style={styles.divider} />

        {/* Result */}
        <div style={styles.result}>
          <div style={styles.resultDate}>
            {diaSemana}, {day} de {MESES[month - 1]} de {year}
          </div>
          <div style={styles.resultSub}>
            {bisiesto ? "Año bisiesto · " : ""}{maxDay} días en {MESES[month - 1]}
          </div>
        </div>
      </div>
    </div>
  );
}

const styles = {
  root: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    padding: "2rem",
    fontFamily: "'DM Sans', 'Segoe UI', sans-serif",
  },
  card: {
    background: "#fff",
    border: "1px solid #e8e6e1",
    borderRadius: 16,
    padding: "1.5rem",
    width: 380,
    boxShadow: "0 2px 12px rgba(0,0,0,0.06)",
  },
  header: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: "1.25rem",
  },
  headerTitle: {
    fontSize: 15,
    fontWeight: 500,
    color: "#1a1a1a",
  },
  todayBtn: {
    fontSize: 12,
    color: "#666",
    background: "none",
    border: "1px solid #ddd",
    borderRadius: 8,
    padding: "4px 12px",
    cursor: "pointer",
  },
  spinners: {
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    gap: 8,
  },
  sep: {
    fontSize: 24,
    color: "#ccc",
    fontWeight: 300,
    paddingBottom: 6,
  },
  segment: {
    display: "flex",
    justifyContent: "center",
  },
  input: {
    fontSize: 20,
    fontWeight: 500,
    color: "#1a1a1a",
    background: "#f7f6f3",
    border: "1px solid #e8e6e1",
    borderRadius: 10,
    padding: "8px 4px",
    textAlign: "center",
    width: "100%",
    outline: "none",
    boxSizing: "border-box",
  },
  arrow: {
    width: 30,
    height: 28,
    borderRadius: 7,
    border: "1px solid #e8e6e1",
    background: "transparent",
    color: "#999",
    cursor: "pointer",
    fontSize: 12,
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    lineHeight: 1,
  },
  labels: {
    display: "flex",
    justifyContent: "center",
    gap: 8,
    marginTop: 6,
    alignItems: "center",
  },
  label: {
    fontSize: 11,
    color: "#aaa",
    textTransform: "uppercase",
    letterSpacing: "0.05em",
    minWidth: 64,
    textAlign: "center",
  },
  divider: {
    height: 1,
    background: "#f0ede8",
    margin: "1.25rem 0",
  },
  result: {
    textAlign: "center",
  },
  resultDate: {
    fontSize: 15,
    fontWeight: 500,
    color: "#1a1a1a",
    marginBottom: 4,
  },
  resultSub: {
    fontSize: 12,
    color: "#999",
  },
};