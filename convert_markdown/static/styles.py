style = """

@page {
    size: A4; 
    margin: 0;
    margin-bottom: 1in; 
    margin-top: 1in;
  }
@page :first {
    margin-top: 0in !important;
}

body {
    font-family: Arial;
    line-height: 1.2;
    margin: 1in;
    max-width: 800px;
    font-size: 1.1em;
    background: #ffffff;
    color: #1c2434;
    text-align: justify;
    hyphens: auto;
}

.chart-container {
    display: block;
    width: 70%;
    margin: 1em auto !important;
    padding: 0 !important;
} """


style1 = """
/* Corporate finance style */
@page {
    size: A4; 
    margin: 0;
    margin-bottom: 1in; 
    margin-top: 1in;
  }
@page :first {
    margin-top: 0in !important;
}
body {
    font-family: Georgia;
    line-height: 1.2;
    margin: 1in;
    max-width: 800px;
    font-size: 1.1em;
    background: #ffffff;
    color: #1c2434;
    text-align: justify;
    hyphens: auto;
}

h1 {
    font-size: 2.2em;
    color: #262a58;
    border-bottom: 2px solid #ddd;
    padding-bottom: 0.3em;
    margin-bottom: 0.34em;
    font-weight: 700;
    text-align: left;
    line-height: 1.2;
}

h2 { 
    font-size: 1.6em;
    color: #262a58;
    margin-top: 0.5em !important;
    margin-bottom: 0.3em !important;
    padding-bottom: 0em !important;
    font-weight: 700;
    letter-spacing: -0.01em;
    text-align: left;
}

h3 {
    font-size: 1.4em;
    color: #262a58;
    margin-top: 0.4em !important;
    margin-bottom: 0.3em !important;
    padding-bottom: 0em !important;
    font-weight: 600;
    text-align: left;
}

p {
    color: #252930;
    /* margin: 1em 0; */
    line-height: 1.4em;
    text-align: justify;
    hyphens: auto;
    margin-top: 0em !important;
    padding-top: 0em !important;
    padding-bottom: 0em !important;
    margin-bottom: 0.4em !important;
}

/* List styling */
ul {
    /* margin: 1.2em 0; */
    margin-top: 0em !important;
    line-height: 0;
    padding-left: 2.5em;
    color: #252930;
    margin-bottom: 0em !important;
}
ol {
    /* margin: 1.2em 0; */
    line-height: 0;
    padding-left: 2.5em;
    color: #252930;
    margin-bottom: 0em !important;
}

li {
    padding-top: 0em !important;
    margin-bottom: 0.4em !important;
    margin-top: 0em !important;
    line-height: 1.4em;
    padding-bottom: 0.3em !important;
    text-align: justify;
    hyphens: auto;
}

ul li, ol li {
    /* margin-bottom: 0.8em; */
    /* line-height: 1.6; */
    padding-left: 0.5em;
}


ul li::marker {
    color: #1f2937;
}

/* Table enhancements */
table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin: 24px 0;
    color: #252930;
    font-size: 0.8em;
    font-family: 'Times New Roman';
    border-radius: 6px;
    
}

th{
    line-height: 1.3em;
    font-weight: 600;
    font-size: 1.1em !important;
    border-bottom: 2px solid #192026;
    border-top: 2px solid #192026;
}

td{
    line-height: 0.9em;
    border-bottom: 2px solid #e0e4e8;
}

th, td {
    padding: 8px 12px;
    font-size: 1.1em;
    
}

th:first-child, td:first-child {
    text-align: left; 
}


tbody tr:hover {
    background-color: #f8fafc;
}


blockquote {
    border-left: 4px solid #1f2937;
    margin: 2em 0;
    padding: 1em 1.5em;
    background: #f8fafc;
    color: #2d3748;
    font-style: italic;
    font-size: 1.1em;
    position: relative;
}

blockquote::before {
    content: '"';
    font-size: 4em;
    color: #1f2937;
    opacity: 0.2;
    position: absolute;
    left: 10px;
    top: -10px;
}

/* Code blocks */
pre, code {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 0.2em 0.4em;
    font-family: 'Consolas', 'Monaco', monospace;
    font-size: 0.9em;
}

pre {
    padding: 1em;
} 
.chart-container {
    display: block;
    width: 70%;
    margin: 1em auto !important;
    padding: 0 !important;
}

/* Add these styles for code output */
.code-output {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 4px;
    padding: 1em;
    margin: 1em 0;
    font-family: 'Consolas', 'Monaco', monospace;
    font-size: 0.9em;
    white-space: pre-wrap;
}

.code-error {
    background: #fff5f5;
    border: 1px solid #feb2b2;
    border-radius: 4px;
    padding: 1em;
    margin: 1em 0;
    font-family: 'Consolas', 'Monaco', monospace;
    font-size: 0.9em;
    color: #c53030;
    white-space: pre-wrap;
}

/* Add these styles for code block output */
.code-block-output {
    display: block;
    margin: 1em 0;
    clear: both;  /* Prevent floating elements from interfering */
}

.code-block-output img {
    display: block;
    margin: 1em auto;  /* Center images */
    max-width: 100%;   /* Ensure images don't overflow */
}

.code-block-output .code-output,
.code-block-output .code-error {
    margin: 0.5em 0;
}
"""

style2 = """
/* Modern business style */
@page {
    size: A4; 
    margin: 0;
    margin-bottom: 1in; 
    margin-top: 1in;
  }
@page :first {
    margin-top: 0in !important;
}

body {
    font-family: 'Lucida Grande';
    line-height: 0.8;
    max-width: 1200px;
    margin: 1in;
    /* padding: 40px; */
    /* background: #ffffff; */
    color: #1f2937;
    font-size: 1em;
}

.chart-container {
    width: 70%;
    /* margin: 2em auto; */
    background: #f9fafb;
    /* border: 1px solid #e5e7eb; */
}

h1 {
    font-size: 2.4em;
    color: #111827;
    margin-bottom: 0.7em;
    line-height: 1.2;
    font-weight: 600;
    letter-spacing: -0.03em;
    position: relative;
    padding-bottom: 0.5em;
}

h1::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 60px;
    height: 4px;
    background: #4f46e5;
}

h2 {
    font-size: 1.8em;
    color: #1f2937;
    margin-top: 0.6em;
    margin-bottom: 0.4em;
    font-weight: 550;
    letter-spacing: -0.01em;
}

h3 {
    font-size: 1.4em;
    color: #374151;
    margin-top: .5em;
    margin-bottom: 0.4em;
    font-weight: 550;
}

p {
    color: #1f2937;
    line-height: 1.5;
    text-align: justify;
    hyphens: auto;
    margin-bottom: 0em !important;
    margin-top: 0em !important;
    padding-top: 0em !important;
    padding-bottom: 0em !important;
}

/* List styling */
ul, ol {
    color: #1f2937;
    padding-left: 1.5em;
    /* margin: 1em 0; */
}

li {
    line-height: 1.5;
    margin-bottom: 0.4em !important;
    margin-top: 0em !important;
    padding-top: 0em !important;
    padding-bottom: 0em !important;
    text-align: justify;
    hyphens: auto;
}

ul li::marker {
    color: #4f46e5;
}

/* Table styling */
table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    /* margin: 2em 0; */
    font-size: 0.9em;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
}

th {
    background: #f9fafb;
    padding: .8em;
    line-height: 1;
    font-weight: 600;
    color: #111827;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-size: 0.85em;
    border-bottom: 2px solid #e5e7eb;
}

td {
    padding: .8em;
    border-bottom: 1px solid #e5e7eb;
    color: #1f2937;
}

tr:last-child td {
    border-bottom: none;
}

tbody tr:hover {
    background: #f9fafb;
}

/* Blockquotes */
blockquote {
    margin: 2em 0;
    padding: 1.5em 2em;
    background: #f9fafb;
    border-left: 4px solid #4f46e5;
    color: #1f2937;
    font-style: italic;
    border-radius: 0 8px 8px 0;
}

/* Code blocks */
pre, code {
    background: #f9fafb;
    border-radius: 6px;
    padding: 0.2em 0.4em;
    font-family: 'Menlo', 'Monaco', monospace;
    font-size: 0.9em;
    color: #4f46e5;
}

pre {
    padding: 1em;
    border: 1px solid #e5e7eb;
}

"""

style3 = """
@page {
    size: A4; 
    margin: 0;
    margin-bottom: 1in; 
    margin-top: 1in;
  }
@page :first {
    margin-top: 0in !important;
}

body {
    font-family: 'Optima';
    margin: 1in;
    max-width: 1200px;
    line-height: 1.2;
    font-size: 1.1em;
}

.content {
    margin: 0 auto;
    width: 100%;
    max-width: 900px;
    font-size: 1.1em;
    color: #000000;
    text-align: justify;
}

h1 { 
    font-size: 2.3em;
    font-weight: bold;
    margin-bottom: .8em;
    margin-top: 0.8em !important;
    color: #000;
    line-height: 1.2;
    text-align: center;
    margin-left: .1em;
    page-break-before: always;
}

h1 + * {
    page-break-before: avoid;
}

.content > h1:first-child {
    page-break-before: avoid;
}

h2 { 
    font-size: 1.6em;
    font-weight: bold;
    border-bottom: 2px solid #ddd;
    padding-bottom: 0.1em;
    margin-top: .4em;
    margin-bottom: .2em !important;
    color: #000;
}

h3 {
    font-size: 1.4em;
    font-weight: bold;
    padding-bottom: 0.1em;
    margin-top: .4em;
    margin-bottom: .2em !important;
    color: #000;
}

h4 {
    font-size: 1.1em;
    font-weight: bold;
    padding-bottom: 0.1em;
    margin-top: 0.4em;
    margin-bottom: .1em !important;
    color: #000;
}

h5 {
    font-size: 1em;
    font-weight: bold;
    padding-bottom: 0.1em;
    margin-top: 0.4em;
    margin-bottom: .1em !important;
    color: #000;
    margin-left: .3em;
}

h6 {
    font-size: 0.9em;
    font-weight: bold;
    padding-bottom: 0.1em;
    margin-bottom: .1em !important;
    color: #000;
    margin-left: .3em;
}

p {
    margin-bottom: 0.3em !important;
    margin-top: 0em !important;
    padding-top: 0em !important;
    padding-bottom: 0em !important;
}

li {
    font-size: 1em;
    margin-bottom: .4em !important;
    margin-top: 0em !important;
    padding-top: 0em !important;
    padding-bottom: 0em !important;
}

ol, ul {
    font-size: 1em;
}

table {
    border-collapse: separate;
    border-spacing: 0;
    width: 99%;
    margin: 0.1em auto;
    margin-top: 0.2em !important;
    font-size: 0.96em;
    line-height: 1.3;
    background: white;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #e0e4e8;
}

td {
    border: none;
    color: #000000;
    border-bottom: 1px solid #e0e4e8;
    padding: 6px 8px;
    text-align: left;
    vertical-align: middle;
    font-size: 1em;
    font-weight: 400;
    background-color: rgba(255, 255, 255, 0.95);
}

th {
    display: table-cell;
    color: #262a58;
    padding: 8px 8px 6px 8px;
    text-align: left;
    background-color: #f8f9fa;
    border-bottom: 2px solid #e0e4e8;
    font-size: 1.05em;
    letter-spacing: 0.01em;
}

tr:last-child td {
    border-bottom: none;
}

td:first-child {
    padding-left: 19px;
    color: #1f2937;
    letter-spacing: -0.01em;
}

th:first-child {
    padding-left: 19px;
    letter-spacing: -0.01em;
}

.chart-container {
    width: 70%;
}

.showdown-chart-error {
    color: #dc2626;
    padding: 12px;
    border: 1px solid #dc2626;
    border-radius: 8px;
    background: #fef2f2;
    margin: 10px 0;
}

"""