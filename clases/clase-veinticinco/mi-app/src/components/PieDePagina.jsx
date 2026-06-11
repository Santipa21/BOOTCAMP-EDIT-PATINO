import React from 'react';

const PieDePagina = () => {
  const styles = {
    footer: {
      background: 'linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)',
      padding: '40px 20px',
      textAlign: 'center',
      color: 'white',
      marginTop: '50px',
      borderTop: '4px solid #667eea'
    },
    content: {
      maxWidth: '1200px',
      margin: '0 auto'
    },
    title: {
      fontSize: '1.8rem',
      fontWeight: 'bold',
      margin: '0 0 15px 0',
      background: 'linear-gradient(90deg, #667eea, #764ba2)',
      WebkitBackgroundClip: 'text',
      WebkitTextFillColor: 'transparent',
      backgroundClip: 'text'
    },
    text: {
      fontSize: '1rem',
      margin: '10px 0',
      opacity: '0.8'
    },
    socialIcons: {
      display: 'flex',
      justifyContent: 'center',
      gap: '20px',
      marginTop: '25px'
    },
    icon: {
      fontSize: '1.5rem',
      cursor: 'pointer',
      transition: 'transform 0.3s ease',
      ':hover': {
        transform: 'scale(1.2)'
      }
    },
    copyright: {
      marginTop: '30px',
      fontSize: '0.9rem',
      opacity: '0.6',
      borderTop: '1px solid rgba(255, 255, 255, 0.1)',
      paddingTop: '20px'
    }
  };

  return (
    <footer style={styles.footer}>
      <div style={styles.content}>
        <h2 style={styles.title}>¡Gracias por visitarnos!</h2>
        <p style={styles.text}>Esta increíble aplicación web fue creada con ❤️</p>
        <p style={styles.text}>Esperamos que disfrutes tu experiencia</p>
        
        <div style={styles.socialIcons}>
          <span style={styles.icon}>🌐</span>
          <span style={styles.icon}>📧</span>
          <span style={styles.icon}>📱</span>
          <span style={styles.icon}>💬</span>
        </div>
        
        <p style={styles.copyright}>
          © 2024 - Todos los derechos reservados
        </p>
      </div>
    </footer>
  );
};

export default PieDePagina;
