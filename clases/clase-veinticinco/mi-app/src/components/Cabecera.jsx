import React from 'react';

class Cabecera extends React.Component {
  render() {
    const styles = {
      header: {
        background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        padding: '40px 20px',
        textAlign: 'center',
        color: 'white',
        boxShadow: '0 4px 15px rgba(0, 0, 0, 0.2)',
        borderRadius: '0 0 20px 20px',
        marginBottom: '30px'
      },
      title: {
        fontSize: '2.5rem',
        fontWeight: 'bold',
        margin: '0 0 10px 0',
        textShadow: '2px 2px 4px rgba(0, 0, 0, 0.3)'
      },
      subtitle: {
        fontSize: '1.2rem',
        margin: '0',
        opacity: '0.9'
      },
      emoji: {
        fontSize: '3rem',
        marginBottom: '15px',
        display: 'block'
      }
    };

    return (
      <header style={styles.header}>
        <span style={styles.emoji}>🚀</span>
        <h1 style={styles.title}>¡Bienvenido a esta increíble aplicación web!</h1>
        <p style={styles.subtitle}>Tu experiencia digital comienza aquí</p>
      </header>
    );
  }
}

export default Cabecera;
