# Netlify Deployment Guide for growwithlumen.com

## Overview
This guide walks you through deploying your Lumen landing page to Netlify and connecting your growwithlumen.com domain purchased from Namecheap.

## Prerequisites
- ✅ Domain: growwithlumen.com (purchased at Namecheap)
- ✅ Landing page files: Located at `/home/ubuntu/lumen-landing-page/`
- ✅ Netlify account (free)

## Step 1: Create Netlify Account
1. Go to [netlify.com](https://netlify.com)
2. Click "Sign up" 
3. Choose "Sign up with email" or use GitHub/GitLab
4. Verify your email address

## Step 2: Deploy Your Landing Page

### Method A: Drag & Drop (Easiest)
1. In Netlify dashboard, look for the deployment area
2. Drag the entire `/home/ubuntu/lumen-landing-page/` folder onto the deployment zone
3. Wait for deployment to complete (usually 1-2 minutes)
4. Netlify will provide a random URL like `https://amazing-name-123456.netlify.app`

### Method B: Git Integration (Recommended for updates)
1. First, push your landing page to a GitHub repository
2. In Netlify: "New site from Git" → Connect to GitHub
3. Select your repository
4. Build settings: Leave blank (static site)
5. Deploy site

## Step 3: Add Custom Domain
1. In your Netlify site dashboard, go to **Site settings**
2. Click **Domain management** in the sidebar
3. Click **Add custom domain**
4. Enter: `growwithlumen.com`
5. Click **Verify**
6. Netlify will show you DNS records to configure

## Step 4: Configure DNS at Namecheap

### Access Namecheap DNS Settings
1. Log into your Namecheap account
2. Go to **Domain List**
3. Click **Manage** next to growwithlumen.com
4. Click **Advanced DNS** tab

### Add DNS Records
Netlify will provide specific records, but typically you'll add:

**For Apex Domain (growwithlumen.com):**
```
Type: A Record
Host: @
Value: 75.2.60.5
TTL: Automatic
```

**For WWW Subdomain:**
```
Type: CNAME Record
Host: www
Value: your-site-name.netlify.app
TTL: Automatic
```

**Alternative: Use Netlify DNS (Easier)**
1. In Netlify domain settings, click **Set up Netlify DNS**
2. Netlify will provide nameservers like:
   - dns1.p01.nsone.net
   - dns2.p01.nsone.net
   - dns3.p01.nsone.net
   - dns4.p01.nsone.net
3. In Namecheap: Domain List → Manage → Nameservers
4. Select **Custom DNS** and enter Netlify's nameservers
5. Save changes

## Step 5: SSL Certificate (Automatic)
- Netlify automatically provides SSL certificates
- Wait 24-48 hours for DNS propagation
- Your site will be available at both:
  - https://growwithlumen.com
  - https://www.growwithlumen.com

## Step 6: Verify Deployment
1. Visit https://growwithlumen.com
2. Check that all sections load correctly:
   - Hero section with logo
   - Features showcase
   - About section
   - Pricing
   - Download buttons
   - Footer
3. Test on mobile devices
4. Verify all links work

## Troubleshooting

### DNS Not Propagating
- DNS changes can take 24-48 hours
- Use [whatsmydns.net](https://whatsmydns.net) to check propagation
- Clear browser cache

### Site Not Loading
- Check DNS records are correct
- Verify domain spelling
- Wait for SSL certificate provisioning

### Images Not Displaying
- Ensure all image files are in the deployed folder
- Check file paths in HTML are relative
- Verify image file extensions match

## Optional: Add SiteLock Security (Later)
Once your site is live, you can optionally add SiteLock for security monitoring:
1. Purchase SiteLock service
2. Configure FTP access for scanning
3. Set up malware monitoring
4. Enable firewall protection

## Performance Optimization
- Netlify automatically optimizes images
- Enables compression
- Provides global CDN
- Minifies CSS/JS

## Analytics Setup (Optional)
Add Google Analytics to track visitors:
1. Create Google Analytics account
2. Add tracking code to `index.html`
3. Monitor traffic and user behavior

## Cost Breakdown
- **Domain**: ~$12/year (already purchased)
- **Netlify Hosting**: Free for basic use
- **SSL Certificate**: Free (included)
- **Total**: $0/month (after domain purchase)

## Support Resources
- **Netlify Docs**: [docs.netlify.com](https://docs.netlify.com)
- **Namecheap Support**: [support.namecheap.com](https://support.namecheap.com)
- **DNS Checker**: [whatsmydns.net](https://whatsmydns.net)

---

Your Lumen landing page will be live at https://growwithlumen.com with professional hosting, automatic SSL, and global CDN delivery! 🚀
