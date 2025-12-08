import requests 
from langchain.tools import tool 
from bs4 import BeautifulSoup
import re

@tool
def trending(query:str) -> str: 
    """This tool returns trending repositories from github given a query parameter.
    Extracts Box-row class elements and article tags from GitHub trending page."""
    try:
        res = requests.get(f'https://github.com/trending/{query}', timeout=30)
        res.raise_for_status()
        
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # Extract elements with Box-row class
        box_rows = soup.find_all(class_='Box-row')
        
        # Extract article tags
        articles = soup.find_all('article')
        
        results = {
            'box_rows': [],
            'articles': []
        }
        
        # Process Box-row elements
        for box_row in box_rows:
            raw_text = box_row.get_text(strip=True)
            results['box_rows'].append({
                'text': raw_text,
                'html': str(box_row)
            })
        
        # Process article elements  
        for article in articles:
            raw_text = article.get_text(strip=True)
            results['articles'].append({
                'text': raw_text,
                'html': str(article)
        })
        
        # Create a clean summary for the LLM
        summary_parts = []
        
        if results['box_rows']:
            summary_parts.append(f"Found {len(box_rows)} Box-row elements:")
            for i, row in enumerate(results['box_rows'][:5], 1):  # Limit to first 5
                text_preview = row['text'][:200] + "..." if len(row['text']) > 200 else row['text']
                summary_parts.append(f"{i}. {text_preview}")
        
        if results['articles']:
            summary_parts.append(f"\nFound {len(articles)} article elements:")
            for i, article in enumerate(results['articles'][:5], 1):  # Limit to first 5
                text_preview = article['text'][:200] + "..." if len(article['text']) > 200 else article['text']
                summary_parts.append(f"{i}. {text_preview}")
        
        return "\n".join(summary_parts) if summary_parts else "No trending repositories found."
                         
    except requests.RequestException as e:
        return f"Error fetching GitHub trending page: {str(e)}"
    except Exception as e:
        return f"Error parsing HTML content: {str(e)}"


if __name__ == '__main__': 
    print(trending('node'))