function TransactionDashboard() {
    const [selectedMonth, setSelectedMonth] = useState('March');
  
    return (
      <div>
        <TransactionTable 
          selectedMonth={selectedMonth} 
          onMonthChange={setSelectedMonth} 
        />
        <TransactionStatistics selectedMonth={selectedMonth} />
        <TransactionsBarChart selectedMonth={selectedMonth} />
      </div>
    );
  }