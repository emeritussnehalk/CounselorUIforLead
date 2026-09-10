import re

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Original content length:", len(content))

# ----------------------------------------------------------------------
# 1. Update the Navigation Bar (<nav role="tablist">)
# ----------------------------------------------------------------------
old_nav_start = content.find('<nav class="flex items-center space-x-1" role="tablist"')
old_nav_end = content.find('</nav>', old_nav_start) + len('</nav>')

print("Found nav from", old_nav_start, "to", old_nav_end)

new_nav = '''<nav class="flex items-center space-x-1 overflow-x-auto" role="tablist" aria-label="Lead Record Tabs">
          <!-- Tab 1: Lead Overview -->
          <button 
            type="button" 
            id="tabBtnOverview"
            onclick="switchLeadTab('overview')" 
            class="flex items-center gap-1.5 px-3.5 py-2.5 text-xs font-bold border-b-2 border-[#0176D3] text-[#0176D3] bg-white rounded-t cursor-pointer transition shadow-2xs whitespace-nowrap"
            role="tab" 
            aria-selected="true"
          >
            <svg class="w-4 h-4 text-[#0176D3]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
            <span>Lead Overview</span>
          </button>
          
          <!-- Tab 2: Lead Details (Refactored Minimal Scroll) -->
          <button 
            type="button" 
            id="tabBtnDetails"
            onclick="switchLeadTab('details')" 
            class="flex items-center gap-1.5 px-3.5 py-2.5 text-xs font-semibold border-b-2 border-transparent text-[#514F4D] hover:text-[#181818] hover:bg-white/60 rounded-t cursor-pointer transition whitespace-nowrap"
            role="tab" 
            aria-selected="false"
          >
            <svg class="w-4 h-4 text-[#706E6B]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
            <span>Lead Details</span>
            <span class="text-[10px] bg-[#706E6B]/10 text-[#514F4D] font-bold px-1.5 py-0.2 rounded-full">9 Cats · 85 Fields</span>
          </button>

          <!-- Tab 3: Documents (NEW) -->
          <button 
            type="button" 
            id="tabBtnDocuments"
            onclick="switchLeadTab('documents')" 
            class="flex items-center gap-1.5 px-3.5 py-2.5 text-xs font-semibold border-b-2 border-transparent text-[#514F4D] hover:text-[#181818] hover:bg-white/60 rounded-t cursor-pointer transition whitespace-nowrap"
            role="tab" 
            aria-selected="false"
          >
            <svg class="w-4 h-4 text-[#706E6B]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
            <span>Documents</span>
            <span class="text-[10px] bg-[#2E844A]/10 text-[#2E844A] font-bold px-1.5 py-0.2 rounded-full">4/6 Verified</span>
          </button>

          <!-- Tab 4: Payments & Financing (NEW) -->
          <button 
            type="button" 
            id="tabBtnPayments"
            onclick="switchLeadTab('payments')" 
            class="flex items-center gap-1.5 px-3.5 py-2.5 text-xs font-semibold border-b-2 border-transparent text-[#514F4D] hover:text-[#181818] hover:bg-white/60 rounded-t cursor-pointer transition whitespace-nowrap"
            role="tab" 
            aria-selected="false"
          >
            <svg class="w-4 h-4 text-[#706E6B]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"/></svg>
            <span>Payments & Fees</span>
            <span class="text-[10px] bg-[#0176D3]/10 text-[#0176D3] font-bold px-1.5 py-0.2 rounded-full">₹25k Paid · Pre-Approved</span>
          </button>
          
          <!-- Tab 5: Lead Activity -->
          <button 
            type="button" 
            id="tabBtnActivity"
            onclick="switchLeadTab('activity')" 
            class="flex items-center gap-1.5 px-3.5 py-2.5 text-xs font-semibold border-b-2 border-transparent text-[#514F4D] hover:text-[#181818] hover:bg-white/60 rounded-t cursor-pointer transition whitespace-nowrap"
            role="tab" 
            aria-selected="false"
          >
            <svg class="w-4 h-4 text-[#706E6B]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            <span>Lead Activity</span>
            <span class="ml-1 text-[10px] bg-[#0176D3]/10 text-[#0176D3] font-bold px-1.5 py-0.2 rounded-full" id="leadActivityCountBadge">7</span>
          </button>
        </nav>'''

content = content[:old_nav_start] + new_nav + content[old_nav_end:]
print("Nav replaced successfully!")

# Write intermediate to verify
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
