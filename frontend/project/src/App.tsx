import React, { useState } from 'react';
import { Sparkles, Instagram, Clock, Hash, PlayCircle, Rocket } from 'lucide-react';
import styles from './styles/App.module.css';
import './styles/global.css';

interface MarketingStrategy {
  hashtags: string[];
  postingTime: string;
  caption: string;
  contentIdeas: string[];
}

function App() {
  const [currentPage, setCurrentPage] = useState<'landing' | 'form' | 'about'>('landing');
  const [isGenerating, setIsGenerating] = useState(false);
  const [strategy, setStrategy] = useState<MarketingStrategy | null>(null);
  const [loadingText, setLoadingText] = useState('');

  const handleGetStarted = () => {
    setCurrentPage('form');
  };

  const handleNavigate = (page: 'landing' | 'form' | 'about') => {
    setCurrentPage(page);
  };

  const cycleLoadingText = () => {
    const texts = [
      "✨ Crafting your perfect Instagram strategy...",
      "🚀 Finding the hottest trends just for you...",
      "🎬 Preparing your marketing masterpiece..."
    ];
    let index = 0;
    const interval = setInterval(() => {
      setLoadingText(texts[index]);
      index = (index + 1) % texts.length;
    }, 2000);
    return () => clearInterval(interval);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsGenerating(true);
    const cleanup = cycleLoadingText();
    
    setTimeout(() => {
      setStrategy({
        hashtags: ['#digitalmarketing', '#instagramgrowth', '#socialmediatips'],
        postingTime: '9:00 PM EST',
        caption: 'Transform your Instagram presence with AI-powered strategies! 🚀',
        contentIdeas: ['Behind-the-scenes Reels', 'Educational Carousel', 'Story Polls'],
      });
      setIsGenerating(false);
      cleanup();
    }, 6000);
  };

  const handleGenerateAgain = () => {
    setStrategy(null);
  };

  if (currentPage === 'landing') {
    return (
      <div className={styles.landingContainer}>
        <div className={styles.landingContent}>
          <div className={`${styles.logo} neon-text`}>
            <Sparkles /> TrendMate
          </div>
          <h1 className={`${styles.landingTitle} neon-text`}>
            Transform Your Instagram Game with AI
          </h1>
          <p className={styles.landingDescription}>
            Create engaging content strategies, optimize your posting schedule, and grow your audience with AI-powered insights.
          </p>
          <button 
            className={`${styles.getStartedButton} neon-button`}
            onClick={handleGetStarted}
          >
            Get Started <Rocket className={styles.buttonIcon} />
          </button>
        </div>
        <div className={styles.landingBackground}>
          <div className={styles.glowOrb}></div>
          <div className={styles.glowOrb}></div>
        </div>
      </div>
    );
  }

  if (currentPage === 'about') {
    return (
      <div className={styles.container}>
        <header className={styles.header}>
          <nav className={`${styles.nav} glass`}>
            <div className={`${styles.logo} neon-text`} onClick={() => handleNavigate('landing')} style={{ cursor: 'pointer' }}>
              <Sparkles /> TrendMate
            </div>
            <div className={styles.navLinks}>
              <a href="#" className={styles.navLink} onClick={() => handleNavigate('landing')}>Home</a>
              <a href="#" className={styles.navLink} onClick={() => handleNavigate('about')}>About</a>
            </div>
          </nav>
        </header>

        <div className={`${styles.aboutContainer} glass`}>
          <h1 className={`${styles.aboutTitle} neon-text`}>About TrendMate</h1>
          <div className={styles.aboutContent}>
            <p>TrendMate is your AI-powered companion for Instagram success. We combine cutting-edge artificial intelligence with deep social media expertise to help you create engaging, trend-setting content that resonates with your audience.</p>
            
            <h2 className="neon-text">Our Mission</h2>
            <p>To democratize social media success by making professional-grade marketing strategies accessible to everyone, from influencers to small businesses.</p>
            
            <h2 className="neon-text">How It Works</h2>
            <ul>
              <li>Advanced AI Analysis of trending content</li>
              <li>Real-time hashtag optimization</li>
              <li>Smart posting time recommendations</li>
              <li>Engaging caption generation</li>
              <li>Custom content strategy creation</li>
            </ul>
            
            <button 
              className={`${styles.getStartedButton} neon-button`}
              onClick={() => handleNavigate('form')}
              style={{ marginTop: '2rem' }}
            >
              Try TrendMate Now <Rocket className={styles.buttonIcon} />
            </button>
          </div>
        </div>

        <footer className={`${styles.footer} glass`}>
          <p>© 2025 The Mate Group. All Rights Reserved.</p>
        </footer>
      </div>
    );
  }

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <nav className={`${styles.nav} glass`}>
          <div className={`${styles.logo} neon-text`} onClick={() => handleNavigate('landing')} style={{ cursor: 'pointer' }}>
            <Sparkles /> TrendMate
          </div>
          <div className={styles.navLinks}>
            <a href="#" className={styles.navLink} onClick={() => handleNavigate('landing')}>Home</a>
            <a href="#" className={styles.navLink} onClick={() => handleNavigate('about')}>About</a>
          </div>
        </nav>
        <h1 className="neon-text" style={{ textAlign: 'center', fontSize: '2.5rem', marginTop: '2rem' }}>
          AI-Powered Instagram Marketing Strategy
        </h1>
      </header>

      <main>
        {isGenerating ? (
          <div className={`${styles.loadingContainer} glass`}>
            <div className={styles.loadingSpinner}></div>
            <p className={styles.loadingText}>{loadingText}</p>
          </div>
        ) : (
          <>
            <form onSubmit={handleSubmit} className={`${styles.form} glass`}>
              <h2 className={styles.formTitle}>Create Your Marketing Strategy</h2>
              
              <div className={styles.inputGroup}>
                <label className={styles.label}>Niche</label>
                <input
                  type="text"
                  placeholder="e.g., Fitness, Fashion, Tech"
                  className={`${styles.input} neon-border`}
                />
              </div>

              <div className={styles.inputGroup}>
                <label className={styles.label}>Target Audience</label>
                <input
                  type="text"
                  placeholder="e.g., Gen Z, Entrepreneurs"
                  className={`${styles.input} neon-border`}
                />
              </div>

              <div className={styles.inputGroup}>
                <label className={styles.label}>Marketing Goal</label>
                <input
                  type="text"
                  placeholder="e.g., Increase Followers, Boost Engagement"
                  className={`${styles.input} neon-border`}
                />
              </div>

              <div className={styles.inputGroup}>
                <label className={styles.label}>Content Type</label>
                <input
                  type="text"
                  placeholder="e.g., Reels, Stories, Carousels"
                  className={`${styles.input} neon-border`}
                />
              </div>

              <button type="submit" className={`${styles.button} neon-button`}>
                Generate Strategy
              </button>
            </form>

            {strategy && (
              <section className={`${styles.results} glass`}>
                <div className={styles.videoPlayer}>
                  <PlayCircle size={64} />
                </div>

                <div className={styles.resultCard}>
                  <h3 className="neon-text">Best Posting Time <Clock size={16} /></h3>
                  <p>{strategy.postingTime}</p>
                </div>

                <div className={styles.resultCard}>
                  <h3 className="neon-text">Trending Hashtags <Hash size={16} /></h3>
                  <div className={styles.hashtags}>
                    {strategy.hashtags.map((tag) => (
                      <span key={tag} className={styles.hashtag}>{tag}</span>
                    ))}
                  </div>
                </div>

                <div className={styles.resultCard}>
                  <h3 className="neon-text">Suggested Caption <Instagram size={16} /></h3>
                  <p>{strategy.caption}</p>
                </div>

                <div className={styles.resultCard}>
                  <h3 className="neon-text">Content Ideas</h3>
                  <ul style={{ marginLeft: '1.5rem' }}>
                    {strategy.contentIdeas.map((idea) => (
                      <li key={idea}>{idea}</li>
                    ))}
                  </ul>
                </div>

                <div className={styles.actionButtons}>
                  <button 
                    onClick={handleGenerateAgain} 
                    className={`${styles.button} neon-button`}
                  >
                    🔄 Generate Again
                  </button>
                  <button className={`${styles.button} neon-button`}>
                    📝 Make Changes
                  </button>
                  <button className={`${styles.button} neon-button`}>
                    🚀 Continue
                  </button>
                </div>
              </section>
            )}
          </>
        )}
      </main>

      <footer className={`${styles.footer} glass`}>
        <p>© 2025 The Mate Group. All Rights Reserved.</p>
      </footer>
    </div>
  );
}

export default App;