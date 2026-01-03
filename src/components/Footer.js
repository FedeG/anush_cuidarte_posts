import React from 'react';
import { Instagram, Mail, Globe } from 'lucide-react';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-section">
          <div className="footer-logo">
            <h3>Anush Cuidarte</h3>
          </div>
          <p className="footer-desc">
            <strong>Hola! Soy Anush Camacho</strong><br />
            Licenciada en Enfermería, puericultora, especialista en lactancia, inmunización y cuidado de heridas en la primera infancia.
          </p>
          <p className="footer-desc">
            Me encontrás en redes como @anush.cuidarte, la EnfermeraPueri.
          </p>
          <p className="footer-desc">
            Trabajo en atención primaria de la salud y acompaño familias en procesos clave como la lactancia, 
            el cuidado del recién nacido, la vacunación respetuosa y la crianza desde una mirada empática, 
            basada en la evidencia y con mucho compromiso.
          </p>
          <p className="footer-cta">
            Creo profundamente en el acompañamiento informado, amoroso y sin recetas únicas. 
            Para mí, la salud se construye en diálogo, desde el respeto por los tiempos y decisiones de cada familia.
          </p>
          <p className="footer-desc" style={{ marginTop: '12px', fontStyle: 'italic' }}>
            Además de atender en consultorio (presencial y virtual), dicto talleres, charlas y creo contenido educativo 
            para redes sociales y plataformas digitales.
          </p>
          <p className="footer-desc" style={{ fontWeight: '600', opacity: '1' }}>
            Gracias por estar acá y confiarme un pedacito de tu camino.
          </p>
        </div>

        <div className="footer-section">
          <h4>Seguime</h4>
          <div className="social-icons">
            <a href="https://www.instagram.com/anush.cuidarte/" target="_blank" rel="noopener noreferrer" className="social-icon instagram">
              <Instagram size={20} />
            </a>
            <a href="https://anush.com.ar/" target="_blank" rel="noopener noreferrer" className="social-icon website">
              <Globe size={20} />
            </a>
          </div>
        </div>

        <div className="footer-section">
          <h4>Contacto</h4>
          <div className="contact-info">
            <a href="mailto:info@anush.com.ar" className="contact-link">
              <Mail size={18} />
              info@anush.com.ar
            </a>
          </div>
        </div>
      </div>

      <div className="footer-bottom">
        <p>&copy; 2026 Anush Cuidarte. Todos los derechos reservados.</p>
      </div>
    </footer>
  );
};

export default Footer;
