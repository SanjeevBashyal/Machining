// Generated from c:\Users\sanje\Desktop\PyParser\Sql.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SqlLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		OID=1, NID=2, GID=3, ID=4, INT=5, STRING=6, COMMENT=7, WS=8;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"OID", "NID", "GID", "ID", "INT", "STRING", "COMMENT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "OID", "NID", "GID", "ID", "INT", "STRING", "COMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public SqlLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Sql.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\nG\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\3\2\3\2\6\2\26"+
		"\n\2\r\2\16\2\27\3\3\3\3\6\3\34\n\3\r\3\16\3\35\3\4\3\4\6\4\"\n\4\r\4"+
		"\16\4#\3\5\3\5\7\5(\n\5\f\5\16\5+\13\5\3\6\6\6.\n\6\r\6\16\6/\3\7\3\7"+
		"\7\7\64\n\7\f\7\16\7\67\13\7\3\7\3\7\3\b\3\b\7\b=\n\b\f\b\16\b@\13\b\3"+
		"\b\3\b\3\t\3\t\3\t\3\t\2\2\n\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\3\2\b"+
		"\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f$$\4\2\f\f\17\17\5\2\13\f\17"+
		"\17\"\"\2M\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2"+
		"\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\23\3\2\2\2\5\31\3\2\2\2\7\37"+
		"\3\2\2\2\t%\3\2\2\2\13-\3\2\2\2\r\61\3\2\2\2\17:\3\2\2\2\21C\3\2\2\2\23"+
		"\25\7Q\2\2\24\26\t\2\2\2\25\24\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27"+
		"\30\3\2\2\2\30\4\3\2\2\2\31\33\7P\2\2\32\34\t\2\2\2\33\32\3\2\2\2\34\35"+
		"\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\6\3\2\2\2\37!\7I\2\2 \"\t\2\2"+
		"\2! \3\2\2\2\"#\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\b\3\2\2\2%)\t\3\2\2&(\t\4"+
		"\2\2\'&\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\n\3\2\2\2+)\3\2\2\2,."+
		"\t\2\2\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\f\3\2\2\2\61\65"+
		"\7$\2\2\62\64\n\5\2\2\63\62\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2\65\66"+
		"\3\2\2\2\668\3\2\2\2\67\65\3\2\2\289\7$\2\29\16\3\2\2\2:>\7*\2\2;=\n\6"+
		"\2\2<;\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?A\3\2\2\2@>\3\2\2\2AB\7+"+
		"\2\2B\20\3\2\2\2CD\t\7\2\2DE\3\2\2\2EF\b\t\2\2F\22\3\2\2\2\n\2\27\35#"+
		")/\65>\3\2\3\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}