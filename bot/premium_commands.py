from telegram import Update
from telegram.ext import ContextTypes
from services.content_optimization import content_optimization_service
from services.advanced_analytics import advanced_analytics_service
from utils.helpers import clean_text, format_message, get_parse_mode

async def optimize_content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please provide some text to optimize.")
        return

    text = ' '.join(context.args)
    cleaned_text = clean_text(text)
    optimized_text, sentiment = content_optimization_service.optimize_content(cleaned_text)
    
    formatted_text = format_message(optimized_text, 'markdown')
    await update.message.reply_text(
        f"Optimized content:\n\n{formatted_text}\n\nSentiment: {sentiment:.2f}",
        parse_mode=get_parse_mode('markdown')
    )

async def generate_analytics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # This is a placeholder. In a real implementation, you'd fetch actual data from your database
    sample_data = [
        {"date": "2023-06-01", "engagement": 100},
        {"date": "2023-06-02", "engagement": 120},
        {"date": "2023-06-03", "engagement": 110},
        {"date": "2023-06-04", "engagement": 130},
        {"date": "2023-06-05", "engagement": 140},
    ]
    
    report = advanced_analytics_service.generate_engagement_report(sample_data)
    await update.message.reply_photo(report, caption="Engagement Report")

async def predict_performance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please provide some text to predict performance for.")
        return

    text = ' '.join(context.args)
    # This is a placeholder. In a real implementation, you'd fetch actual historical data
    sample_historical_data = [
        {"performance": 100},
        {"performance": 120},
        {"performance": 110},
        {"performance": 130},
        {"performance": 140},
    ]
    
    prediction = advanced_analytics_service.predict_content_performance(sample_historical_data, text)
    await update.message.reply_text(f"Predicted performance: {prediction:.2f}")

