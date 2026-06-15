// ===== Blog Posts Data =====
const blogPosts = [
  {
    title: "From Logistics to AI: My Career Transition Journey",
    date: "2026-06-10",
    category: "Career",
    excerpt: "After 10 years in marketing management and logistics, I decided to pivot into AI training. Here's what I learned about data annotation, prompt evaluation, and how my operations background became my biggest advantage in AI quality assurance."
  },
  {
    title: "What I Learned from Annotating 5,000+ Data Points",
    date: "2026-05-28",
    category: "AI Training",
    excerpt: "Data annotation is more than labeling — it's about understanding context, following guidelines precisely, and maintaining consistency. Here are the key lessons from my hands-on experience with text classification and sentiment analysis projects."
  },
  {
    title: "5 Tips for Landing Your First AI Trainer Role",
    date: "2026-05-15",
    category: "Tips",
    excerpt: "Platforms like TELUS International and Outlier are actively hiring AI trainers. Based on my experience applying and interviewing, here are 5 practical tips to help you stand out — even without a technical degree."
  }
];

// ===== Render Blog Posts =====
function renderBlog() {
  const container = document.getElementById('blogGrid');
  if (!container) return;

  container.innerHTML = blogPosts.map(post => `
    <article class="blog-card">
      <div class="blog-meta">
        <span class="blog-category">${post.category}</span>
        <time class="blog-date" datetime="${post.date}">${formatDate(post.date)}</time>
      </div>
      <h3 class="blog-title">${post.title}</h3>
      <p class="blog-excerpt">${post.excerpt}</p>
    </article>
  `).join('');
}

function formatDate(dateStr) {
  const date = new Date(dateStr);
  return date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
}

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', renderBlog);
